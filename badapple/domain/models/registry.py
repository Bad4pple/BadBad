from badapple.domain.models.order import OrderingRepository

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            assert not args and not kwargs
        return cls._instances[cls]

class __RepositoriesRegistry(metaclass=Singleton):
    def __init__(self) -> None:
        self.__order_repositry: OrderingRepository | None = None

    @property
    def order_service(self):
        return self.__order_repositry

    @order_service.setter
    def order_service(self, adapter):
        self.__order_repositry = adapter

repo = __RepositoriesRegistry()

