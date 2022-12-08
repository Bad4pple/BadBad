from badapple.adapter import InmemoryAdapter
from badapple.domain.models.registry import repo

def inject_adapter() -> None: 
    repo.order_service = InmemoryAdapter()


