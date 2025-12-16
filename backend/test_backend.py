import requests

BASE_URL = "http://localhost:8000/api"  # backend kontin portti

def test_index():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "Hello from MySQL" in data["message"], f"Unexpected message: {data}"

def test_time():
    r = requests.get(f"{BASE_URL}/time/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "time" in data["message"], f"Missing 'time' in response: {data}"

def test_health():
    r = requests.get(f"{BASE_URL}/health/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert data["message"]["status"] == "ok", f"Unexpected health status: {data}"

if __name__ == "__main__":
    test_index()
    test_time()
    test_health()
    print("All backend tests passed ✅")
