FROM python:3.9-slim

# Install supervisor and bash
RUN apt-get update && apt-get install -y supervisor bash

RUN mkdir myapp

# Work directory
WORKDIR /myapp

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy other project files
COPY . .

# Uncomment and add environment variables here
# ARG DATABASE_URI
# ENV DATABASE_URI=${DATABASE_URI}

# Run database migrations
RUN python manage.py db upgrade

# Start the application
RUN python manage.py run

# Expose a port to Containers
EXPOSE 80

# Start supervisor with the specified configuration file
CMD bash -c "supervisord -c supervisord.conf"```