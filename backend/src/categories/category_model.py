from uuid import UUID

from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from src.models import BaseORM


class CategoriesORM(BaseORM):
    uuid: Mapped[UUID] = mapped_column(
        primary_key=True, index=True
    )  # primary key, identificator of category
    category_name: Mapped[str] = mapped_column(
        VARCHAR(100), unique=True
    )  # name of category
