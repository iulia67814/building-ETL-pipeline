FROM python:3.8-buster

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["python3", "./main.py"]