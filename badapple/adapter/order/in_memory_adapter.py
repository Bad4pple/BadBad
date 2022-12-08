from badapple.domain.models.order import OrderingRepository

class InmemoryAdapter(OrderingRepository):
    def __init__(self) -> None:
        self.db = []

# bug 
        

    def new(self,order_line):
        self.db.append(order_line)

    def from_id(self,id):
        # return index for index i 
        # print("GGEZ: ",self.db)
        for index in self.db:
            if index["order_id"] == id:
                return index
        return None

    def save(self,entity):
        print(self.from_id(entity["order_id"]))

        