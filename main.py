from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app.routes.transcribe import router as transcribe_router

app = FastAPI(
    title="Video a PDF - Transcriptor de YouTube",
    description="API para convertir videos de YouTube a PDF o HTML usando subtítulos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(transcribe_router)


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join("outputs", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    media_type = "text/html" if filename.endswith('.html') else "application/pdf"
    return FileResponse(file_path, media_type=media_type, filename=filename)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
