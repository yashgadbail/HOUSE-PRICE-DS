import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home():
    response = requests.get(BASE_URL + "/")
    assert response.status_code == 200

def test_prediction():
    data = {"location": "Aundh", "bhk": 2, "bath": 2, "sqft": 1000}
    response = requests.post(BASE_URL + "/predict", data=data)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
