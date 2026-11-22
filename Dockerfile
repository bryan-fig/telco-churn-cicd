FROM python:3.11-slim
# Imagen con Python
WORKDIR /app
# Directorio interno
COPY requirements.txt ./
# Dependencias primero para aprovechar caché
RUN pip install --no-cache-dir -r requirements.txt
# Instalar paquetes
COPY app/ ./app/
# Copiar aplicación
COPY models/ ./models/
# Copiar modelo
COPY templates/ ./templates/
# Copiar interfaz
EXPOSE 8000
# Puerto interno
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Iniciar servicio
