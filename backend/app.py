from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Config
from utils import create_directories

from routes.upload import router as upload_router
from routes.detect import router as detect_router
from routes.chat import router as chat_router
from routes.report import router as report_router


create_directories()

app = FastAPI(
    title=Config.APP_NAME,
    version=Config.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)

app.include_router(
    detect_router,
    prefix="/detect",
    tags=["Detection"]
)

app.include_router(
    chat_router,
    prefix="/chat",
    tags=["Chat"]
)

app.include_router(
    report_router,
    prefix="/report",
    tags=["Report"]
)


@app.get("/")
def home():
    return {
        "application": Config.APP_NAME,
        "version": Config.VERSION,
        "status": "Running 🚀"
    }