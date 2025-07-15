from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def create_user(self, user_data: UserCreate):
        return self.repository.create(user_data)

    def get_user(self, user_id: int):
        return self.repository.get(user_id)

    def get_users(self):
        return self.repository.list()

    def update_user(self, user_id: int, user_data: UserCreate):
        user = self.repository.get(user_id)
        return self.repository.update(user, user_data)

    def delete_user(self, user_id: int):
        user = self.repository.get(user_id)
        self.repository.delete(user)
