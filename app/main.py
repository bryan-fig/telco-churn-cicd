from pathlib import Path  # Rutas portables
import joblib  # Leer pipeline entrenado
import pandas as pd  # Preparar datos
from fastapi import FastAPI  # API web
from fastapi.responses import HTMLResponse  # Formulario HTML
from app.schemas import CustomerInput  # Esquema de cliente

BASE_DIR = Path(__file__).resolve().parent.parent  # Raíz del proyecto
MODEL_PATH = BASE_DIR / "models" / "champion.joblib"  # Artefacto
model = joblib.load(MODEL_PATH)  # Cargar una vez
app = FastAPI(title="Telco Churn API", version="1.0")  # Crear API

@app.get("/health")  # Endpoint de disponibilidad
async def health():  # Responder estado
    return {"status": "ok"}  # Respuesta sencilla

@app.get("/", response_class=HTMLResponse)  # Formulario
async def home():  # Servir página
    return (BASE_DIR / "templates" / "index.html").read_text(encoding="utf-8")  # HTML

@app.post("/predict")  # Endpoint de inferencia
async def predict(customer: CustomerInput):  # Validar entrada
    frame = pd.DataFrame([customer.model_dump()])  # Una fila con columnas
    prediction = int(model.predict(frame)[0])  # Clase binaria
    probability = float(model.predict_proba(frame)[0, 1])  # Probabilidad clase 1
    risk = "Bajo" if probability < 0.30 else "Medio" if probability < 0.70 else "Alto"  # Bandas ilustrativas
    return {"prediction": prediction, "churn_probability": probability, "risk_level": risk, "message": "Cliente con riesgo de abandono" if prediction else "Cliente con bajo riesgo de abandono"}  # JSON
