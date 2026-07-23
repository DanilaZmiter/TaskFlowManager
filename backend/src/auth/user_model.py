from typing import Optional
from uuid import UUID

from pydantic import EmailStr
from sqlalchemy import TEXT, VARCHAR, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models import BaseORM


class UsersORM(BaseORM):
    uuid: Mapped[UUID] = mapped_column(
        primary_key=True, default=func.gen_random_uuid(), unique=True, index=True
    )  # primary key, user identification
    email: Mapped[EmailStr] = mapped_column(
        VARCHAR(255), unique=True, index=True
    )  # email used for login, user identification
    username: Mapped[str] = mapped_column(
        VARCHAR(100), unique=True, index=True
    )  # unique person's username, user identification
    first_name: Mapped[Optional[str]] = mapped_column(
        VARCHAR(100), default=None
    )  # person's first name
    last_name: Mapped[Optional[str]] = mapped_column(
        VARCHAR(100), default=None
    )  # person's last name
    description: Mapped[Optional[str]] = mapped_column(
        TEXT, default=None
    )  # description of person
    is_superuser: Mapped[bool] = mapped_column(
        default=False
    )  # status of administration level
    is_verified: Mapped[bool] = mapped_column(default=False)  # status of verifing
    password_hash: Mapped[str] = mapped_column(
        VARCHAR(255),
    )  # hash of the password
