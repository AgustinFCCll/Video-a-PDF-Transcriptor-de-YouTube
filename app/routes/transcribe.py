from fastapi import APIRouter, HTTPException
from app.models.request_models import VideoRequest, VideoResponse
from app.services.video_service import VideoService

router = APIRouter()
video_service = VideoService()


@router.post("/convert", response_model=VideoResponse)
async def convert_video(request: VideoRequest):
    try:
        result = video_service.process_video(
            url=request.url,
            lang=request.lang,
            as_html=request.as_html
        )

        return VideoResponse(
            success=True,
            message=f"{result['file_type'].upper()} generado exitosamente",
            file_path=result["output_path"],
            file_size=result["file_size"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
