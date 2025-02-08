FROM python:3.11-slim

WORKDIR /app

COPY ./app /app

# Instalar dependencias
RUN pip install --no-cache-dir fastapi uvicorn httpx python-jose[cryptography] passlib[bcrypt]

# Asegúrate de que Uvicorn apunte al módulo correcto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
