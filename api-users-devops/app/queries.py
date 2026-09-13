from sqlalchemy.orm import Session
from app.models import User

class UserQueryService:
    def __init__(self, db: Session):
        self.db = db

    def handle_get_all_users(self) -> list[User]:
        return self.db.query(User).all()

    def handle_get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()