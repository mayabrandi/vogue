#!/usr/bin/env python

from flask import render_template, Blueprint, current_app, request

from vogue.constants.constants import YEARS
from vogue import __version__

app = current_app
cancer_blueprint = Blueprint('cancer', __name__)


@cancer_blueprint.route('/Bioinfo/Cancer/<year>')
def balsamic(year: int):

    return render_template('balsamic.html',
                           header='Balsamic',
                           endpoint=request.endpoint,
                           version=__version__,
                           year_of_interest=year,
                           years=YEARS)
