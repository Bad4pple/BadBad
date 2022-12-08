from badapple.domain.models.registry import repo
from .order_id import ObjectID
from .price import Prices
from datetime import datetime
# from badapple.domain.models.order import OrderService

class OrderService:
   def create_new_order(self,order_line):
      total_price = Prices(order_line.items).calculate_total_price()
      obj = {
         "order_id": ObjectID().generate_id(),
         "items": order_line.items,
         "total_prices": total_price,
         "status": "waiting",
         "timestamp": datetime.now()
      }
      repo.order_service.new(obj)
      # print(a)
      # print(Prices(order_line.items).calculate_total_price())
      return obj
      
   def get_order(self,_id):
        order = repo.order_service.from_id(_id)
        return order
   
   def submit(self,_id):
      order = repo.order_service.from_id(_id)
      if not order:
         return False

      order["status"] = "pending"
      repo.order_service.save(order)