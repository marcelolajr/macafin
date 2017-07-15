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
    params = flask.request.form
    report = cash_basis_generation(params['start'], params['end'], app)
    return flask.render_template('cash_basis.html', object=report)


@app.errorhandler(404)
def page_not_found(error):
    """
        Error view handler
    """
    return flask.render_template('404.html', error=error)
