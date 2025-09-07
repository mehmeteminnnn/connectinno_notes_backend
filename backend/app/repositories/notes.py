from __future__ import annotations

from datetime import datetime, timezone
from typing import List

from google.cloud.firestore import Client
from google.cloud import firestore as gc_firestore

from ..models.note import NoteCreate, NoteOut, NoteUpdate


class NotesRepository:
	def __init__(self, db: Client) -> None:
		self.db = db
		self.collection_name = "notes"

	def _user_collection(self, user_id: str):
		return self.db.collection(self.collection_name).document(user_id).collection("items")

	def list_notes(self, user_id: str) -> List[NoteOut]:
		query = self._user_collection(user_id).order_by("updated_at", direction=gc_firestore.Query.DESCENDING)
		docs = query.stream()
		results: List[NoteOut] = []
		for d in docs:
			data = d.to_dict() or {}
			results.append(
				NoteOut(
					id=d.id,
					title=data.get("title", ""),
					content=data.get("content", ""),
					created_at=data.get("created_at"),
					updated_at=data.get("updated_at"),
				)
			)
		return results

	def create_note(self, user_id: str, payload: NoteCreate) -> str:
		now = datetime.now(timezone.utc)
		ref = self._user_collection(user_id).document()
		ref.set(
			{
				"title": payload.title,
				"content": payload.content,
				"created_at": now,
				"updated_at": now,
			}
		)
		return ref.id

	def update_note(self, user_id: str, note_id: str, payload: NoteUpdate) -> None:
		update_data = {k: v for k, v in payload.model_dump().items() if v is not None}
		update_data["updated_at"] = datetime.now(timezone.utc)
		self._user_collection(user_id).document(note_id).update(update_data)

	def delete_note(self, user_id: str, note_id: str) -> None:
		self._user_collection(user_id).document(note_id).delete()


