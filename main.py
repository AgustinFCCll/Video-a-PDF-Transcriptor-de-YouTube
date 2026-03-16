import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from app.core import create_app
from app.routes import transcribe

app = create_app()

app.include_router(transcribe.router)


@app.get("/")
async def root():
    return {"message": "Video a PDF API", "docs": "/docs"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join("outputs", filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    
    media_type = "text/html" if filename.endswith(".html") else "application/pdf"
    return FileResponse(file_path, media_type=media_type, filename=filename)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
