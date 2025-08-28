# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copia requirements e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

# Expõe porta do Fly
ENV PORT=8080

# Comando padrão
CMD ["gunicorn", "vibora.wsgi:application", "--bind", "0.0.0.0:8080"]
