# Base Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the local app.py to the container
COPY app.py /app/app.py

# Install required Python packages with a specific version of pandas
RUN pip install pandas==1.5.3

# Command to run the application
CMD ["python", "app.py"]
