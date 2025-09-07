from __future__ import annotations

import firebase_admin
from firebase_admin import auth as firebase_auth
from firebase_admin import credentials
from google.cloud import firestore

from ..core.config import settings


_firebase_app: firebase_admin.App | None = None
_firestore_client: firestore.Client | None = None


def initialize_firebase() -> None:
	global _firebase_app, _firestore_client
	if _firebase_app is not None:
		return

	private_key = settings.firebase_private_key.replace("\\n", "\n") if settings.firebase_private_key else ""
	cred = credentials.Certificate(
		{
			"type": "service_account",
			"project_id": settings.firebase_project_id,
			"private_key_id": "2218b694dba6e1269ff83c4eef73ff2bf919b6c7",
			"private_key": private_key,
			"client_email": settings.firebase_client_email,
			"client_id": "113215315816194225410",
			"auth_uri": "https://accounts.google.com/o/oauth2/auth",
			"token_uri": "https://oauth2.googleapis.com/token",
			"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
			"client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{settings.firebase_client_email}",
		    "universe_domain": "googleapis.com"
		}

	)
	_firebase_app = firebase_admin.initialize_app(cred, options={"projectId": settings.firebase_project_id})
	_firestore_client = firestore.Client(project=settings.firebase_project_id)


def get_firestore_client() -> firestore.Client:
	if _firestore_client is None:
		initialize_firebase()
	return _firestore_client  # type: ignore[return-value]


def verify_id_token(id_token: str) -> dict:
	initialize_firebase()
	return firebase_auth.verify_id_token(id_token)


