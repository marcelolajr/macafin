"""
    does nothing
"""
import flask
import config
app = flask.Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object(config.Development)
# app.config.from_object(config.Production)


@app.route('/')
def index():
    """
        does nothing
    """
    return flask.render_template('index.html')

# sass --watch macafin.scss:static/css/macafin.css
