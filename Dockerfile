# set base image (host OS)
FROM python:3.9.13

# set the working directory in the container
WORKDIR /code

# set the port
EXPOSE 5000

# copy the dependencies file to the working directory
COPY requirements.txt .

# copy the content of the local src directory to the working directory
COPY src/ .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "./server.py" ]