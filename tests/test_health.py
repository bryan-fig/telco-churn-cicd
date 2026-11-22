from fastapi.testclient import TestClient  # Cliente de prueba
from app.main import app  # Aplicación
client = TestClient(app)  # Cliente local

def test_health():  # Verificar salud
    response = client.get("/health")  # Solicitud GET
    assert response.status_code == 200 
    assert response.json() == {"status": "ok"}  # Contenido correcto

def test_home():  # Verificar interfaz
    response = client.get("/")  # Solicitud HTML
    assert response.status_code == 200  # HTTP correcto
    assert "Telco Churn Predictor" in response.text  # Contenido presente
