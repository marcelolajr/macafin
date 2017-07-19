# -*- coding: utf-8 -*-
"""
    Macafin app file
    ~~~~~~~~~

    This module implements the central WSGI application object.

    :copyright: (c) 2017 by Aguiar, Vitoriano.
    :license: GNU GPL 3, see LICENSE for more details.
"""
import flask
import config
from cash_basis import cash_basis_generation
app = flask.Flask(__name__)
app.config.from_object(config.Development)
# app.config.from_object(config.Production)


@app.route('/', methods=['GET'])
def index():
    """
        Index view handler
    """
    return flask.render_template('index.html')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
        Dashboard view handler
    """
    return flask.render_template('dashboard.html')


@app.route('/report', methods=['GET'])
def report():
    """
        Report view handler
    """
    return flask.render_template('report.html')


@app.route('/report_generation', methods=['POST'])
def report_generation():
    """
        Report generation handler
    """
    params = flask.request.form
    report = cash_basis_generation(params['start'], params['end'], app)
    return flask.render_template('cash_basis.html', object=report)


@app.route('/settings', methods=['GET'])
def settings():
    """
        Settings view handler
    """
    return flask.render_template('settings.html')


@app.route('/about', methods=['GET'])
def about():
    """
        About view handler
    """
    return flask.render_template('about.html')


@app.route('/legal_information', methods=['GET'])
def legal_information():
    """
        Legal information generation handler
    """
    return flask.render_template('legal_information.html')


@app.errorhandler(404)
def page_not_found(error):
    """
        Error view handler
    """
    return flask.render_template('404.html', error=error)
