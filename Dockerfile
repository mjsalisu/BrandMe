# Base Image
FROM python:3.9-slim

# Install supervisor and bash
RUN apt-get update && apt-get install -y supervisor bash

RUN mkdir app

# Work directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy other project files
COPY . .

# Uncomment and add environment variables here
# ARG DATABASE_URI
# ENV DATABASE_URI=${DATABASE_URI}

# Run Flask database upgrade
RUN flask db upgrade
RUN python manage.py

# Expose a port to Containers 
EXPOSE 80

# Start supervisor with the specified configuration file
CMD bash -c "supervisord -c supervisord.conf" 