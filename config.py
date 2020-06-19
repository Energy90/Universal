import os

class Config(object):
    # the secrete key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cc6e2a7a076e4989a4171f132bd897cd'

    SIJAX_STATIC_PATH = 'app/static/js/sijax'
    SIJAX_JSON_URI = 'app/static/js/sijax/json2.js'

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    