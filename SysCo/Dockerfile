FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./SysCo/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./SysCo /app

CMD ["python", "manage.py", "test"]
