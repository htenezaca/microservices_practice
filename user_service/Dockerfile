FROM python:3.11-slim

WORKDIR /app

# Copia la carpeta app en el directorio de trabajo
COPY app /app/app

# Instalar dependencias necesarias
RUN pip install --no-cache-dir fastapi uvicorn httpx python-jose[cryptography] passlib[bcrypt] python-multipart bcrypt==4.0.1

# Ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
