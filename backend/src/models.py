from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class BaseORM(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__[:-3].lower()

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated__at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
