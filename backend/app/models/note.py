from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
	title: str = Field(min_length=1, max_length=200)
	content: str = Field(default="")


class NoteUpdate(BaseModel):
	title: str | None = Field(default=None, min_length=1, max_length=200)
	content: str | None = None


class NoteOut(BaseModel):
	id: str
	title: str
	content: str
	created_at: datetime
	updated_at: datetime


