FROM python:3.10.6-alpine

WORKDIR . .

COPY ./SysCo/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . . 

CMD ["python", "manage.py", "test"]
