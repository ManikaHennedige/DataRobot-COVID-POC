# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the Docker container
WORKDIR /app

# Copy the current directory (i.e., your Flask app) into the container at /app
COPY . /app/
COPY start_server.sh /opt/code/

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements-docker.txt

# Expose port for the app to listen on
EXPOSE 8080

# Run your Flask application
ENTRYPOINT ["./start_server.sh"]