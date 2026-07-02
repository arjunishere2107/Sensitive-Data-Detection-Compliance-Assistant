import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = "Sensitive Data Detection & Compliance Assistant"

    VERSION = "1.0"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile"
    )

    UPLOAD_DIR = "uploads"

    VECTOR_DB_DIR = "vector_db"

    REPORT_DIR = "reports"