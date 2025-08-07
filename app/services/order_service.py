from sqlalchemy.orm import Session

from app.repositories.order_repository import OrderRepository
from app.schemas.order_schema import OrderCreate

class OrderService:
    def __init__(self, db: Session):
        self.repository = OrderRepository(db)

    def create_order(self, order_data: OrderCreate):
        return self.repository.create(order_data)

    def get_order(self, order_id: int):
        return self.repository.get(order_id)

    def get_orders(self):
        return self.repository.list()

    def update_order(self, order_id: int, order_data: OrderCreate):
        order = self.repository.get(order_id)
        return self.repository.update(order, order_data)

    def delete_order(self, order_id: int):
        order = self.repository.get(order_id)
        self.repository.delete(order)
