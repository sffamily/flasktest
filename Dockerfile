# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the entrypoint command to run the Flask app
#CMD ["python", "app.py"]
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]