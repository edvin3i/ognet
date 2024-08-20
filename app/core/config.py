from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # DB settings
    DATABASE_URL: str = Field("sqlite:///./test.db", env='DATABASE_URL')

    # email settings
    # SMTP_SERVER: str = Field(..., env='SMTP_SERVER')
    # SMTP_PORT: int = Field(..., env='SMTP_PORT')
    # SMTP_USER: str = Field(..., env='SMTP_USER')
    # SMTP_PASSWORD: str = Field(..., env='SMTP_PASSWORD')
    # EMAIL_FROM: str = Field(..., env='EMAIL_FROM')
    # EMAIL_TO: str = Field(..., env='EMAIL_TO')

    class Config:
        env_file = '.env'

settings = Settings()
