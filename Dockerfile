# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /phonebook
WORKDIR /phonebook

# Copy the current directory contents into the container at /app
ADD . /phonebook

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "phonebook.py"]

