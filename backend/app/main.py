from fastapi import FastAPI
from .api.routes import notes


def create_app() -> FastAPI:
	app = FastAPI(title="ConnectInno Notes API", version="0.3.0")

	# Routers (Firestore tabanlı)
	app.include_router(notes.router)

	@app.get("/health")
	def health_check():
		return {"status": "ok"}

	return app


app = create_app()


