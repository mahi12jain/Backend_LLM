# # Use an official Python image as the base
# FROM python:3.11-slim

# # Set environment variables to prevent Python from generating .pyc files and enable unbuffered logging
# ENV PYTHONUNBUFFERED=1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file
# COPY requirements.txt /app/

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the backend code
# # (Note: in Docker Compose development mode, this will be volume-mounted)
# COPY . .

# # Expose the port FastAPI will run on
# EXPOSE 8000

# # Command to run the FastAPI server
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Groq API Key
ARG GROQ_API_KEY
ENV GROQ_API_KEY=${GROQ_API_KEY}

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]