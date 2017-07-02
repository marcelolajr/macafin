"""
    does nothing
"""
import flask
app = flask.Flask(__name__) # pylint: disable=invalid-name
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def index():
    """
        does nothing
    """
    return flask.render_template('index.html')

# sass --watch macafin.scss:static/css/macafin.css