from . database import Base
from sqlalchemy import Integer, String, TIMESTAMP, Enum as SQLAlchemyEnum, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, Relationship
from pydantic import EmailStr, BaseModel
from typing import Optional
from sqlalchemy import text
from datetime import datetime
from enum import Enum



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))


# Task Model
#id, title, content, priority, deadline, type, Task_status
class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum(str, Enum):
    todo = "todo"
    completed = "completed"
    overdue = "overdue"

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    priority: Mapped[Optional[PriorityEnum]] = mapped_column(
        SQLAlchemyEnum(PriorityEnum),
        default=PriorityEnum.medium,
        nullable=True
    )
    status: Mapped[StatusEnum] = mapped_column(
        SQLAlchemyEnum(StatusEnum),
        default=StatusEnum.todo
    )
    deadline: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    creator = Relationship("User")