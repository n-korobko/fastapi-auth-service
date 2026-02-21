from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.services.user import create_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_user = await create_user(db, user)
        return new_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=UserResponse)
async def login(user_data: UserLogin, db: AsyncSession = Depends(get_db)):

    user = await authenticate_user(db, user_data.email, user_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    return user