import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import transcribe


@pytest.fixture
def client():
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(transcribe.router)
    
    @app.get("/health")
    async def health():
        return {"status": "ok"}
    
    @app.get("/")
    async def root():
        return {"message": "Video a PDF API"}
    
    return TestClient(app)


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_convert_endpoint_exists(client):
    response = client.post("/convert", json={
        "url": "https://youtube.com/watch?v=TEST",
        "lang": "es",
        "as_html": False
    })
    assert response.status_code != 404


def test_convert_invalid_url(client):
    response = client.post("/convert", json={
        "url": "invalid_url",
        "lang": "es",
        "as_html": False
    })
    assert response.status_code in [400, 500]


def test_download_endpoint_not_found(client):
    response = client.get("/download/nonexistent.pdf")
    assert response.status_code == 404


def test_video_request_model():
    from app.models.request_models import VideoRequest
    
    req = VideoRequest(url="https://youtube.com/watch?v=TEST")
    assert req.url == "https://youtube.com/watch?v=TEST"
    assert req.lang == "es"
    assert req.as_html == False
    
    req = VideoRequest(url="https://youtube.com/watch?v=TEST", lang="en", as_html=True)
    assert req.lang == "en"
    assert req.as_html == True


def test_video_service_initialization():
    from app.services.video_service import VideoService
    
    service = VideoService()
    assert service.output_dir == "outputs"


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
