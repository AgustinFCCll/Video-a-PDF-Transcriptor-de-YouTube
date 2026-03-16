from pydantic import BaseModel


class VideoRequest(BaseModel):
    url: str
    lang: str = "es"
    as_html: bool = False


class VideoResponse(BaseModel):
    success: bool
    message: str
    file_path: str
    file_size: int = 0
