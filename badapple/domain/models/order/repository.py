from abc import ABC , abstractmethod

class OrderingRepository(ABC):

    @abstractmethod
    def from_id(id):
        pass

    @abstractmethod
    def save(self, entity):
        pass 
