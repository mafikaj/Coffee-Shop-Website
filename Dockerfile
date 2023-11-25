# Use an official Python runtime as a parent image
FROM python:3.8

# Install system-level dependencies
RUN apt-get update && \
    apt-get install -y some-package

# Create a non-root user
RUN useradd -ms /bin/bash myuser

# Set the working directory and ownership
WORKDIR /app
COPY . /app

# Exclude files mentioned in .gitignore
COPY .dockerignore /app/.dockerignore
RUN cat /app/.dockerignore | xargs rm -rf

RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
