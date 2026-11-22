from fastapi.testclient import TestClient  # Cliente de pruebas
from app.main import app  # Aplicación
client = TestClient(app)  # Cliente local
SAMPLE = {"tenure": 5, "MonthlyCharges": 85.5, "TotalCharges": 427.5, "Contract": "Month-to-month", "InternetService": "Fiber optic"}  # Datos válidos

def test_predict():  # Probar predicción
    response = client.post("/predict", json=SAMPLE)  # Enviar cliente
    assert response.status_code == 200  # HTTP correcto
    body = response.json()  # Leer respuesta
    assert body["prediction"] in (0, 1)  # Clase válida
    assert 0 <= body["churn_probability"] <= 1  # Probabilidad válida
    assert body["risk_level"] in ("Bajo", "Medio", "Alto")  # Banda válida

def test_invalid_input():  # Validación de Pydantic
    response = client.post("/predict", json={**SAMPLE, "tenure": -10})  # Dato inválido
    assert response.status_code == 422  # Rechazo esperado
