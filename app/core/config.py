from pydantic import BaseSettings, Field

class Seetings(BaseSettings):
    # DB settings
    DATABASE_URL: str = Field(..., env='DATABASE_URL')

    # email settings
    SMTP_SERVER: str = Field(..., env='SMTP_SERVER')
    SMTP_PORT: int = Field(..., env='SMTP_PORT')
    SMTP_USER: str = Field(..., env='SMTP_USER')
    SMTP_PASSWORD: str = Field(..., env='SMTP_PASSWORD')
    EMAIL_FROM: str = Field(..., env='EMAIL_FROM')
    EMAIL_TO: str = Field(..., env='EMAIL_TO')

    class Config:
        env_file = '.env'

settings = Seetings()
