from badapple.domain import usecase
from badapple.api.schemas import order

from fastapi import APIRouter , status , HTTPException

router = APIRouter()



@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(order_line_request: order.OrderLineInSchema):
    order_id = await usecase.create_new_order(order_line_request)
    return order_id

# @router.get("/")
# async def get_order():
#     orders = await usecase.get_order("2")
#     return orders

@router.get("/{id}")
async def get_order(id: str):
    order = await usecase.get_order_from_id(id)
    # print("a",order)
    # print(type(order))
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    return order

@router.put("/submission/{id}")
async def submission(id: str):
    order_status = await usecase.submission_order(id)
    return order_status