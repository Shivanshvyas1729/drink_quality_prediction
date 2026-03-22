# Use official Python 3.8.5 slim image based on Debian Buster (lightweight base)
FROM python:3.8.5-slim-buster

# Set working directory inside container to /app
WORKDIR /app

# Copy only requirements.txt first (enables better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application source code into working directory
COPY . .

# Default command to run the application
CMD ["python", "app.py"]
          