# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /code
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .
# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
