from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.video_a_pdf import process_video

app = FastAPI(title="Video a PDF API")


class VideoRequest(BaseModel):
    url: str
    lang: str = "es"
    as_html: bool = False


@app.post("/convert")
async def convert_video(request: VideoRequest):
    try:
        result = process_video(
            url=request.url,
            lang=request.lang,
            as_html=request.as_html
        )

        return {
            "success": True,
            "message": f"{result['file_type'].upper()} generado exitosamente",
            "file_path": result["output_path"],
            "file_size": result["file_size"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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