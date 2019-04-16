from vogue.server import create_app
from vogue.commands.base import cli
from vogue.adapter.plugin import VougeAdapter

app = create_app(test=True)


def test_analysis(database, get_valid_json):
    app.db = database
    app.adapter = VougeAdapter(database.client, db_name=database.name)

    # GIVEN a correct formatted input file VALID_JSON
    sample_id = 'some_id'

    # WHEN adding a new analysis
    runner = app.test_cli_runner()
    result = runner.invoke(
        cli,
        ['load', 'analysis', '-s', sample_id, '-a', get_valid_json, '-t', 'QC'])

    # THEN assert the new apptag should be added to the colleciton
    assert isinstance(app.adapter.analysis(sample_id), dict)


def test_analysis_no_file(database):
    app.db = database
    app.adapter = VougeAdapter(database.client, db_name=database.name)

    # GIVEN a invalid path to a json file
    sample_id = 'some_id'
    json_path = '/invalid_path_to_json/wrong.json'

    # WHEN adding a new analysis
    runner = app.test_cli_runner()
    result = runner.invoke(
        cli, ['load', 'analysis', '-s', sample_id, '-a', json_path, '-t', 'QC'])

    # THEN assert  Can not load json. Exiting.
    assert result.exit_code == 1


def test_analysis_invalid_file(database, get_invalid_json):
    app.db = database
    app.adapter = VougeAdapter(database.client, db_name=database.name)

    # GIVEN a invalid path to a json file
    sample_id = 'some_id'

    # WHEN adding a new analysis
    runner = app.test_cli_runner()
    result = runner.invoke(
        cli,
        ['load', 'analysis', '-s', sample_id, '-a', get_invalid_json, '-t', 'QC'])

    # THEN assert  Can not load json.
    assert result.exit_code == 1