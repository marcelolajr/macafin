"""
    does nothing
"""
import sys
import flask
import config
from cash_basis import cash_basis_generation
app = flask.Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object(config.Development)
# app.config.from_object(config.Production)


@app.route('/')
def index():
    """
        Index view handler
    """
    return flask.render_template('index.html')


@app.route('/report', methods=['POST'])
def report():
    """
        Report generation handler
    """
    params = flask.request.form  # contains the configuration form params
    # params['start'] and params['end']
    # there's a couple more values, but I don't know why

    # here you should do something like
    report_ = cash_basis_generation(params['start'], params['end'], app)
    # report_ should be the report name as a string

    # this next line would cause it to be downloaded automagically
    return report_


@app.errorhandler(404)
def page_not_found(error):
    """
        Error view handler
    """
    return flask.render_template('404.html', error=error), 404
