"""
    register api to admin blueprint
    ~~~~~~~~~
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint


def create_cms():
    cms = Blueprint('cms', __name__)
    from .admin import admin_api
    from .user import user_api
    from .log import log_api
    from .file import file_api
    from .test import test_api
    from .comm import comm_api
    admin_api.register(cms)
    user_api.register(cms)
    log_api.register(cms)
    file_api.register(cms)
    test_api.register(cms)
    comm_api.register(cms)
    return cms
