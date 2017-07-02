"""
    does nothing
"""
from __future__ import print_function  # In python 2.7
import sys
import flask
import config
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
    # report_ = report_generation(toDate(params['start'], toDate(params['start']))
    # report_ should be the report name as a string
    report_ = ''  # remove this line when you have the previous working

    # this next line would cause it to be downloaded automagically
    return flask.send_from_directory(
        app.config['REPORTS_FOLDER'],
        report_,
        as_attachment=True)


@app.errorhandler(404)
def page_not_found(error):
    """
        Error view handler
    """
    return flask.render_template('404.html', error=error), 404
