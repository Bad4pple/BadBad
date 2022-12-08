from fastapi import APIRouter 
from badapple.api.routers import order

router = APIRouter()

router.include_router(router=order.router, prefix="/order", tags=["Order Service"])