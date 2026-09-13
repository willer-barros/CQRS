from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import CreateUserCommand, UserReadModel
from app.commands import UserCommandService
from app.queries import UserQueryService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
def create_user(command: CreateUserCommand, db: Session = Depends(get_db)):
    command_service = UserCommandService(db)
    return command_service.handle_create_user(command)

@router.get("/", response_model=list[UserReadModel])
def list_users(db: Session = Depends(get_db)):
    query_service = UserQueryService(db)
    return query_service.handle_get_all_users()

@router.get("/{user_id}", response_model=UserReadModel)
def get_user(user_id: int, db: Session = Depends(get_db)):
    query_service = UserQueryService(db)
    user = query_service.handle_get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user