from __future__ import annotations

from fastapi import Depends, Header, HTTPException, status

from ..services.firebase import verify_id_token


async def get_current_user(authorization: str | None = Header(default=None)) -> dict:
	if not authorization:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header missing")

	parts = authorization.split()
	if len(parts) != 2 or parts[0].lower() != "bearer":
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header")

	token = parts[1]
	try:
		claims = verify_id_token(token)
	except Exception:  # pragma: no cover - simplify for case
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

	if "uid" not in claims:
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")

	return claims


