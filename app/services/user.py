from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from passlib.context import CryptContext

from app.models.user import User
from app.schemas.user import UserCreate


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    result = await db.execute(select(User).where(User.email == user_data.email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise ValueError("Email already registered")

    new_user = User(
        name=user_data.name,
        surname=user_data.surname,
        email=user_data.email,
        date_of_birth=user_data.date_of_birth,
        password_hash=hash_password(user_data.password),
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def authenticate_user(db, email: str, password: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user