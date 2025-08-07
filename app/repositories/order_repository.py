from sqlalchemy.orm import Session

from app.models.order import Order
from app.schemas.order_schema import OrderCreate

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, order: OrderCreate):
        db_order = Order(item=order.item, quantity=order.quantity)
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get(self, order_id: int):
        return self.db.query(Order).filter(Order.id == order_id).first()

    def list(self):
        return self.db.query(Order).all()

    def update(self, order: Order, order_data: OrderCreate):
        order.item = order_data.item
        order.quantity = order_data.quantity
        self.db.commit()
        self.db.refresh(order)
        return order

    def delete(self, order: Order):
        self.db.delete(order)
        self.db.commit()
