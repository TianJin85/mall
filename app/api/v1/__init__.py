"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from flask import Blueprint
from app.api.v1 import user, product, order, footprint, evaluate, collect, cart, address


def create_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api_user.register(bp_v1)
    product.api_product.register(bp_v1)
    order.api_order.register(bp_v1)
    footprint.api_footprint.register(bp_v1)
    evaluate.api_evaluate.register(bp_v1)
    collect.api_collect.register(bp_v1)
    cart.api_cart.register(bp_v1)
    address.api_address.register(bp_v1)
    return bp_v1
