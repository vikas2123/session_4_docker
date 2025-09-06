FROM python:3.10-slim

WORKDIR /flask-loan-app

COPY artefacts/requirements.txt .

RUN pip install -r /flask-loan-app/requirements.txt

COPY . /flask-loan-app/

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]