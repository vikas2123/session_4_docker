FROM python:3.10-slim

#inside the dockerhub webside I had searched the python and I got the slim whuch represents the python image with slimos

WORKDIR /flask-loan-app

#Inside SLIM OS create the root working directory naemed as flask-loan-app

COPY artefacts/requirements.txt .

#copy the requirements.txt file from artefacts folder to the working directory inside the docker image

RUN pip install -r /flask-loan-app/requirements.txt

#install all the dependencies mentioned inside the requirements.txt file that we have copied inside the docker image

COPY . /flask-loan-app/

# copy all the files from the current directory to the working directory inside the docker image

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]

#run the flask application using the CMD command and expose it to the host machine on port 8000 i.e our container runs on  port 8000
