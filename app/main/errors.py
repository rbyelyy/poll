__author__ = 'rbs'

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return 'Das ist 404'

@main.app_errorhandler(500)
def internal_server_error(e):
    return 'Das ist 500'