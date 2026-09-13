from sqlalchemy.orm import Session
from app.models import User
from app.schemas import CreateUserCommand

class UserCommandService:
    def __init__(self, db: Session):
        self.db = db

    def handle_create_user(self, command: CreateUserCommand) -> User:
        new_user = User(name=command.name, age=command.age)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user