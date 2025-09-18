import requests


def test_health_endpoint():
    """Checks the FastAPI health endpoint is reachable and returns status ok.

    Note: run the backend locally first: `uvicorn app:app --port 8000` from src/backend
    """
    resp = requests.get("http://localhost:8000/health", timeout=3)
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body, dict)
    assert body.get("status") == "ok"
