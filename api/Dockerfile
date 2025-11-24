# Use a slim Python image for smaller size
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV MODEL_PATH /app/model/gpt2

# Install system dependencies (optional, but good practice)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     ... \
#     && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy model artifacts into the container
# NOTE: In a real-world scenario, you'd download the model from Azure Storage
# or an MLflow registry during the build/startup to keep the image small.
COPY api/model/gpt2 /app/model/gpt2

# Copy requirements and install
COPY api/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the application code
COPY api/app.py /app/app.py

# Expose the port the app runs on
EXPOSE 5000

# Run the application using a more robust server (gunicorn is preferred, but Flask is simpler)
CMD ["python", "app.py"]