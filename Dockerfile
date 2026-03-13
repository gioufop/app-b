# Etapa 1: Build
FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagem final (leve)
FROM python:3.11-alpine
WORKDIR /root/
# Copia as dependências instaladas
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
# Copia o código da aplicação
COPY main.py .
COPY main_test.py .
EXPOSE 8080
CMD ["python", "main.py"]