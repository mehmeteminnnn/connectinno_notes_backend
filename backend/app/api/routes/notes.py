from __future__ import annotations

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from ...api.deps import get_current_user
from ...models.note import NoteCreate, NoteOut, NoteUpdate
from ...repositories.notes import NotesRepository
from ...services.firebase import get_firestore_client


router = APIRouter(prefix="/notes", tags=["notes"])


def get_repo() -> NotesRepository:
	db = get_firestore_client()
	return NotesRepository(db)


@router.get("/", response_model=List[NoteOut])
def list_notes(user=Depends(get_current_user), repo: NotesRepository = Depends(get_repo)):
	return repo.list_notes(user_id=user["uid"]) 


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, user=Depends(get_current_user), repo: NotesRepository = Depends(get_repo)):
	new_id = repo.create_note(user_id=user["uid"], payload=payload)
	return {"id": new_id}


@router.put("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_note(note_id: str, payload: NoteUpdate, user=Depends(get_current_user), repo: NotesRepository = Depends(get_repo)):
	try:
		repo.update_note(user_id=user["uid"], note_id=note_id, payload=payload)
	except Exception:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
	return None


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: str, user=Depends(get_current_user), repo: NotesRepository = Depends(get_repo)):
	try:
		repo.delete_note(user_id=user["uid"], note_id=note_id)
	except Exception:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
	return None


