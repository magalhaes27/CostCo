FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./SysCo/requirements.txt requirements.txt
RUN pip install -r requirements.txt

<<<<<<< HEAD
COPY . /app 
=======
COPY . ./app
>>>>>>> fearure1

CMD ["python", "manage.py", "test"]
