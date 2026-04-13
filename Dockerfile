FROM public.ecr.aws/docker/library/python:3.9-slim

WORKDIR /app

# Install dependencies first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Then copy app
COPY app.py .

CMD ["python", "app.py"]
