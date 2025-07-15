from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def list(self):
        return self.db.query(User).all()

    def update(self, user: User, user_data: UserCreate):
        user.name = user_data.name
        user.email = user_data.email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()
