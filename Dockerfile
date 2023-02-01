# Use an official Python runtime as the base image
#FROM python:3.9-alpine

# Set the working directory in the image
#WORKDIR /app

# Copy the requirements.txt file to the image
#COPY requirements.txt .

# Install the required packages
#RUN pip install -r requirements.txt

# Copy the rest of the application code to the image
#COPY . .

# Define the command to run the program
#CMD ["python3", "comp_intrest.py"]

FROM python

ADD comp_intrest.py .

RUN pip install requests beautifulsoup4 python-dotenv

CMD [ "python", "./comp_intrest.py"]