"""
    Configuration enviroments
"""
from os.path import expanduser


class Development():
    """
        Configuration used for development status
    """

    DEBUG = True
    # TESTING = None
    # PROPAGATE_EXCEPTIONS = None
    # PRESERVE_CONTEXT_ON_EXCEPTION = None
    # SECRET_KEY = None
    # SESSION_COOKIE_NAME = None
    # SESSION_COOKIE_DOMAIN = None
    # SESSION_COOKIE_PATH = None
    # SESSION_COOKIE_HTTPONLY = None
    # SESSION_COOKIE_SECURE = None
    # PERMANENT_SESSION_LIFETIME = None
    # SESSION_REFRESH_EACH_REQUEST = None
    # USE_X_SENDFILE = None
    # LOGGER_NAME = None
    # LOGGER_HANDLER_POLICY = None
    # SERVER_NAME = None
    # APPLICATION_ROOT = None
    # MAX_CONTENT_LENGTH = None
    # SEND_FILE_MAX_AGE_DEFAULT = None
    # TRAP_HTTP_EXCEPTIONS = None
    # TRAP_BAD_REQUEST_ERRORS = None
    # PREFERRED_URL_SCHEME = None
    # JSON_AS_ASCII = None
    # JSON_SORT_KEYS = None
    # JSONIFY_PRETTYPRINT_REGULAR = None
    # SONIFY_MIMETYPE = None
    TEMPLATES_AUTO_RELOAD = True
    # EXPLAIN_TEMPLATE_LOADING = None
    REPORTS_FOLDER = expanduser('~') + '/Macafin'

    def __init__(self):
        pass


class Production():
    """
        Configuration used for production status
    """

    DEBUG = True
    # TESTING = None
    # PROPAGATE_EXCEPTIONS = None
    # PRESERVE_CONTEXT_ON_EXCEPTION = None
    # SECRET_KEY = None
    # SESSION_COOKIE_NAME = None
    # SESSION_COOKIE_DOMAIN = None
    # SESSION_COOKIE_PATH = None
    # SESSION_COOKIE_HTTPONLY = None
    # SESSION_COOKIE_SECURE = None
    # PERMANENT_SESSION_LIFETIME = None
    # SESSION_REFRESH_EACH_REQUEST = None
    # USE_X_SENDFILE = None
    # LOGGER_NAME = None
    # LOGGER_HANDLER_POLICY = None
    # SERVER_NAME = None
    # APPLICATION_ROOT = None
    # MAX_CONTENT_LENGTH = None
    # SEND_FILE_MAX_AGE_DEFAULT = None
    # TRAP_HTTP_EXCEPTIONS = None
    # TRAP_BAD_REQUEST_ERRORS = None
    # PREFERRED_URL_SCHEME = None
    # JSON_AS_ASCII = None
    # JSON_SORT_KEYS = None
    # JSONIFY_PRETTYPRINT_REGULAR = None
    # SONIFY_MIMETYPE = None
    TEMPLATES_AUTO_RELOAD = True
    # EXPLAIN_TEMPLATE_LOADING = None
    REPORTS_FOLDER = expanduser('~') + '/Macafin'

    def __init__(self):
        pass
