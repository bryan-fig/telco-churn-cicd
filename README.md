# Práctica 8 — CI/CD con GitHub Actions

Proyecto **completo y ejecutable** para Windows + Visual Studio Code. **Los datos del entrenamiento son sintéticos**; no se utiliza el CSV oficial de Telco Churn. El objetivo es aprender CI/CD, no producir un modelo comercial.

## 1. Ejecutar localmente (CMD de VS Code)

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m pytest -v
python -m uvicorn app.main:app --reload
```

Abrir `http://127.0.0.1:8000/`, `/docs` y `/health`.

## 2. Probar Docker

```bat
docker build -t telco-api:v1 .
docker run --rm -p 8000:8000 --name telco-api telco-api:v1
```

En otra terminal, abrir `http://127.0.0.1:8000/docs`. Detener con Ctrl+C.

## 3. Publicar en GitHub

Crear un repositorio **vacío** `telco-churn-cicd` en GitHub. Sustituir `TU_USUARIO`:

```bat
git init -b main
git add .
git commit -m "Proyecto inicial CI CD"
git remote add origin https://github.com/TU_USUARIO/telco-churn-cicd.git
git push -u origin main
```

En la pestaña **Actions** observar los jobs `test` y `docker`. La publicación ocurre **solo en push a main** después de que pasen las pruebas. En un Pull Request se ejecutan pruebas, pero no se publica la imagen.

## 4. Provocar y corregir un error

En `tests/test_health.py`, sustituir `assert response.status_code == 200` por `assert response.status_code == 404`; guardar, commit y push. Comprobar que `test` falla y `docker` no se ejecuta. Restaurar `200`, commit y push; comprobar ejecución exitosa.

## 5. Descargar desde GHCR

El paquete publicado se llama `ghcr.io/tu_usuario/telco-churn-cicd:latest` (minúsculas). Si es privado, configurar permisos/autenticación antes de descargar.

```bat
docker pull ghcr.io/tu_usuario/telco-churn-cicd:latest
docker run --rm -p 8000:8000 ghcr.io/tu_usuario/telco-churn-cicd:latest
```

## 6. Evidencias

Capturas de: pruebas locales; workflow exitoso; workflow fallido; workflow corregido; paquete GHCR; predicción desde contenedor.

## Notas importantes

- El modelo `models/champion.joblib` **ya está entrenado** e incluye `ColumnTransformer` y `LogisticRegression` en un `Pipeline`; las transformaciones se ajustaron solo con datos de entrenamiento.
- El modelo usa cinco variables: `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `InternetService`.
- No se debe utilizar el modelo con clientes reales: sus datos de entrenamiento son artificiales.
- Los rangos de dependencias facilitan la práctica; para producción, fijar versiones exactas y hashes y verificar reproducibilidad.
- El workflow realiza CI y publicación (Continuous Delivery), **no despliegue automático a producción**.
