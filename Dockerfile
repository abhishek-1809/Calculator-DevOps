# FROM ubuntu:latest

# Install dos2unix utility
# RUN apt-get update && apt-get install -y dos2unix

# Set the working directory
# WORKDIR /app

# Copy the calculator.sh script into the container
# COPY calculator.sh /app/calculator.sh

# Convert line endings to Unix-style
# RUN dos2unix /app/calculator.sh

# Ensure the script has execute permissions
# RUN chmod +x /app/calculator.sh

# Set the default command to execute calculator.sh
# CMD ["bash", "/app/calculator.sh"]


FROM ubuntu:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the calculator.py script into the container
COPY calculator.py /app/calculator.py

# Install any required Python packages (if needed)
# RUN pip3 install <package-name>

# Set the default command to execute calculator.py
CMD ["python3", "/app/calculator.py"]
