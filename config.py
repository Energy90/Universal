import os

class Config(object):
    # the secrete key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cc6e2a7a076e4989a4171f132bd897cd'

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    