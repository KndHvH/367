# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container

COPY . .

RUN pip3 install -r requirements.txt

# Run the script
CMD ["python", "app.py"]
