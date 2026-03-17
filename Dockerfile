# Use Python 3.10
FROM python:3.10-bullseye

WORKDIR /app

# Install system packages for scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel
RUN pip install --upgrade pip setuptools wheel

# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /app

# Expose Flask port
EXPOSE 5000

# Run the Flask API
CMD ["python", "app.py"]