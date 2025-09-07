from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

	firebase_project_id: str
	firebase_private_key: str
	firebase_client_email: str

	openai_api_key: str | None = None


settings = Settings( firebase_project_id="", firebase_private_key="", firebase_client_email="", )

