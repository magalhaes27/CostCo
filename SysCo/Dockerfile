FROM python:3.10.6-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./app

CMD ["python", "manage.py", "test"]
