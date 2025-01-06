# Use Python base image
FROM python:3.13.1-alpine3.21

# Set the working directory inside the container (it will be created if not present)
WORKDIR /test


# Copy the application files into the container
COPY . /test/

# Install dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8080

# Command to run your Flask app
ENTRYPOINT [ "python3" ]
CMD [ "index.py" ]
