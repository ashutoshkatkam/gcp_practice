# Use a suitable Python base image
FROM python:3.9 

# Set the working directory
WORKDIR /app  

# Copy requirements file 
COPY requirements.txt . 

# Install dependencies
RUN pip install google-cloud-logging

# Copy all application files
COPY . .  


