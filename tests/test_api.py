import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health endpoint returns ok status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_convert_endpoint_exists():
    """Test that /convert endpoint exists"""
    response = client.post("/convert", json={
        "url": "https://youtube.com/watch?v=TEST",
        "lang": "es",
        "as_html": False
    })
    # Should not be 404 (endpoint exists)
    assert response.status_code != 404


def test_convert_invalid_url():
    """Test convert with invalid URL"""
    response = client.post("/convert", json={
        "url": "invalid_url",
        "lang": "es",
        "as_html": False
    })
    # Should return error (not found subtitles or invalid URL)
    assert response.status_code in [400, 500]


def test_download_endpoint_not_found():
    """Test download endpoint with non-existent file"""
    response = client.get("/download/nonexistent_file.pdf")
    assert response.status_code == 404


def test_video_request_model():
    """Test VideoRequest model"""
    from app.models.request_models import VideoRequest
    
    # Test with default values
    req = VideoRequest(url="https://youtube.com/watch?v=TEST")
    assert req.url == "https://youtube.com/watch?v=TEST"
    assert req.lang == "es"
    assert req.as_html == False
    
    # Test with custom values
    req = VideoRequest(url="https://youtube.com/watch?v=TEST", lang="en", as_html=True)
    assert req.lang == "en"
    assert req.as_html == True


def test_video_service_initialization():
    """Test VideoService can be initialized"""
    from app.services.video_service import VideoService
    
    service = VideoService()
    assert service.output_dir == "outputs"
