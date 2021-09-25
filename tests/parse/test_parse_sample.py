from datetime import datetime as dt
from vogue.parse.build.sample import (
    get_number_of_days,
    get_output_artifact,
    get_latest_input_artifact,
    str_to_datetime,
    get_concentration_and_nr_defrosts,
    get_final_conc_and_amount_dna,
    get_microbial_library_concentration,
    get_library_size,
)

############################# get_number_of_days ############################


def test_get_number_of_days_no_date():
    # GIVEN a date that is None
    first_date = None
    second_date = dt.today()

    # WHEN counting the number of days between two dates
    nr_days = get_number_of_days(first_date, second_date)

    # THEN assert nr_days is none
    assert nr_days is None


def test_get_number_of_days():
    # GIVEN two date time dates differing by two days
    first_date = dt.strptime("2018-05-31", "%Y-%m-%d")
    second_date = dt.strptime("2018-06-02", "%Y-%m-%d")

    # WHEN counting the number of days between two dates
    nr_days = get_number_of_days(first_date, second_date)

    # THEN assert nr_days == 2
    assert nr_days == 2


############################# get_output_artifact ############################


def test_get_latest_output_artifact_no_art(lims):
    # GIVEN a lims with no artifacts

    lims_id = "Dummy"
    process_type = "CG002 - Aggregate QC (Library Validation)"

    # WHEN running _get_latest_output_artifact
    latest_output_artifact = get_output_artifact(process_type, lims_id, lims, last=True)

    # THEN assert latest_output_artifact is none
    assert latest_output_artifact is None


def test_get_latest_output_artifact(lims, lims_sample):
    # GIVEN a lims with artifacts A1,A2,A3 and processes P1, P2,P3 with relationships:
    # P1 --> A1
    # P2 --> A2
    # P3 --> A3
    # where P1, P2, P3 are of the same type but have different date_run dates:
    # 2018-01-01, 2018-02-01, 2018-03-01

    lims_id = "Dummy"
    process_type_name = "CG002 - Aggregate QC (Library Validation)"
    process_type = lims._add_process_type(name=process_type_name)
    date1, date2, date3 = "2018-01-01", "2018-02-01", "2018-03-01"

    P1 = lims._add_process(date1, process_type)
    P2 = lims._add_process(date2, process_type)
    P3 = lims._add_process(date3, process_type)
    A1 = lims._add_artifact(P1, samples=[lims_sample])
    A2 = lims._add_artifact(P2, samples=[lims_sample])
    A3 = lims._add_artifact(P3, samples=[lims_sample])

    # WHEN running _get_latest_output_artifact
    latest_output_artifact = get_output_artifact(process_type_name, lims_sample.id, lims, last=True)

    # THEN latest_output_artifact should be run on 2018-03-01
    assert latest_output_artifact.parent_process.date_run == date3


############################# get_latest_input_artifact ############################


def test_get_latest_input_artifact(lims):
    # GIVEN a lims with artifacts A1,A2,A3,A4,A5 and processes P1, P2,P3 with relationships:
    # P1 --> A1
    # P2 --> A2
    # [A4, A5] --> P3 --> A3
    # where P1, P2, P3 are of the same process type but where run on different
    # dates: 2018-01-01, 2018-02-01, 2018-03-01. P3 has the latest date
    # And only A4 has a sample list with a sample with sample_id = TheOne

    sample_id = "TheOne"
    process_type_name = "CG002 - Aggregate QC (Library Validation)"
    process_type = lims._add_process_type(name=process_type_name)
    date1, date2, date3 = "2018-01-01", "2018-02-01", "2018-03-01"

    S1 = lims._add_sample(sample_id=sample_id)
    S2 = lims._add_sample(sample_id="Dummy")

    P1 = lims._add_process(date1, process_type)
    P2 = lims._add_process(date2, process_type)
    P3 = lims._add_process(date3, process_type)

    A1 = lims._add_artifact(parent_process=P1, samples=[S1])
    A2 = lims._add_artifact(parent_process=P2, samples=[S1])
    A3 = lims._add_artifact(parent_process=P3, samples=[S1])

    A4 = lims._add_artifact(samples=[S1])
    A5 = lims._add_artifact(samples=[S2])

    A3.input_list = [A4, A5]

    # WHEN running get_latest_input_artifact
    latest_input_artifact = get_latest_input_artifact(process_type_name, sample_id, lims)

    # THEN latest_input_artifact should be A4
    assert latest_input_artifact == A4


############################# get_concentration_and_nr_defrosts ############################
def test_get_concentration_and_nr_defrosts(lims, lims_sample):
    # GIVEN a lims with artifacts: A1, A2 and processes: P1, P2, P3, P4
    # whith relationship: P1 --> A1 --> P4 --> A2
    # where A1 holds the concentration and P1, P2 and P3 holds the same lotnumber: '12345'
    # and where P2 and P3 were run before P1 (older date_run values)

    lotnumber = "12345"
    application_tag = "WGSPCF"

    lot_nr_step_type = lims._add_process_type(
        name="CG002 - End repair Size selection A-tailing and Adapter ligation (TruSeq PCR-free DNA)"
    )
    lot_nr_udf = "Lot no: TruSeq DNA PCR-Free Sample Prep Kit"
    P1 = lims._add_process(date_str="1919-01-01", process_type=lot_nr_step_type)
    P1.udf[lot_nr_udf] = lotnumber
    P2 = lims._add_process(date_str="1819-01-01", process_type=lot_nr_step_type)
    P2.udf[lot_nr_udf] = lotnumber
    P3 = lims._add_process(date_str="1719-01-01", process_type=lot_nr_step_type)
    P3.udf[lot_nr_udf] = lotnumber

    A1 = lims._add_artifact(parent_process=P1, samples=[lims_sample])
    A1.udf["Concentration (nM)"] = 12

    concentration_step_type = lims._add_process_type(
        name="CG002 - Aggregate QC (Library Validation)"
    )
    P4 = lims._add_process(date_str="1818-01-01", process_type=concentration_step_type)
    P4.input_artifact_list.append(A1)

    A2 = lims._add_artifact(parent_process=P4, samples=[lims_sample])
    A2.input_list.append(A1)

    # WHEN running get_concentration_and_nr_defrosts
    result_dict = get_concentration_and_nr_defrosts(application_tag, lims_sample.id, lims)

    # THEN concentration should be 12 and nr_defrosts 3
    assert result_dict["concentration"] == 12 and result_dict["nr_defrosts"] == 3


############################# get_final_conc_and_amount_dna ############################


def test_get_final_conc_and_amount_dna(lims, lims_sample):
    # GIVEN a lims with artifacts: A1, A2, A3, and processes: P1 and P2
    # whith relationship: A1 --> P1 --> A2 --> P2 --> A3
    # where A1 holds the amount udf and A2 holds the concentration

    application_tag = "WGSLIF"

    A1 = lims._add_artifact(samples=[lims_sample], id="A1")
    A1.udf["Amount (ng)"] = 11

    amount_step_type = lims._add_process_type(name="CG002 - Aggregate QC (DNA)")
    P1 = lims._add_process(date_str="1919-01-01", process_type=amount_step_type, pid="P1")
    P1.input_artifact_list.append(A1)

    A2 = lims._add_artifact(parent_process=P1, samples=[lims_sample], id="A2")
    A2.udf["Concentration (nM)"] = 22
    A2.input_list.append(A1)

    concentration_step_type = lims._add_process_type(
        name="CG002 - Aggregate QC (Library Validation)"
    )
    P2 = lims._add_process(date_str="1919-01-01", process_type=concentration_step_type, pid="P2")
    P2.input_artifact_list.append(A2)

    A3 = lims._add_artifact(samples=[lims_sample], id="A3", parent_process=P2)
    A3.input_list.append(A2)

    # WHEN running get_final_conc_and_amount_dna
    return_dict = get_final_conc_and_amount_dna(application_tag, lims_sample.id, lims)

    # THEN  return_dict should be {'amount': 11, 'concentration': 22}
    assert return_dict == {"amount": 11, "concentration": 22}


############################# get_microbial_library_concentration ############################


def test_get_microbial_library_concentration(lims):
    # GIVEN a lims with artifacts A1,A2,A3,A4,A5 and processes P1, P2,P3 with relationships:
    # P1 --> A1
    # P2 --> A2
    # [A4, A5] --> P3 --> A3
    # where P1, P2, P3 are of the same process type but where run on different
    # dates: 2018-01-01, 2018-02-01, 2018-03-01. P3 has the latest date
    # And only A4 has a sample list with a sample with sample_id = TheOne

    application_tag = "ABCNXUU"

    process_type = lims._add_process_type(name="CG002 - Aggregate QC (Library Validation)")
    concentration_udf = "Concentration (nM)"
    date1, date2, date3 = "2018-01-01", "2018-02-01", "2018-03-01"

    sample_id = "TheOne"
    S1 = lims._add_sample(sample_id=sample_id)
    S2 = lims._add_sample(sample_id="Dummy")

    P1 = lims._add_process(date1, process_type)
    P2 = lims._add_process(date2, process_type)
    P3 = lims._add_process(date3, process_type)

    A1 = lims._add_artifact(parent_process=P1, samples=[S1])
    A2 = lims._add_artifact(parent_process=P2, samples=[S1])
    A3 = lims._add_artifact(parent_process=P3, samples=[S1])

    A4 = lims._add_artifact(samples=[S1], udf={concentration_udf: 12})

    A5 = lims._add_artifact(samples=[S2], udf={concentration_udf: 210})

    A3.input_list = [A4, A5]

    # WHEN running get_microbial_library_concentration
    concentration = get_microbial_library_concentration(application_tag, sample_id, lims)

    # THEN the concentration should be fetched from A4
    assert concentration == 12


