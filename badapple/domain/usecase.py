# from badapple.domain.models.registry import repo
from badapple.domain.models.order import OrderService

async def create_new_order(order_line):
    order_id = OrderService().create_new_order(order_line)
    return order_id

async def get_order_from_id(_id):
    order = OrderService().get_order(_id)
    return order

async def submission_order(_id):
    order = OrderService().submit(_id)
    return order