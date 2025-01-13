# Base Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the local app.py to the container
COPY app.py /app/app.py

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install specific versions of numpy and pandas for compatibility
RUN pip install numpy==1.21.6 pandas==1.3.5

# Command to run the application
CMD ["python", "app.py"]
