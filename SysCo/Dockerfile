FROM python:3.10.6-alpine

WORKDIR ./SysCo

COPY ./SysCo/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./SysCo . 

CMD ["python", "manage.py", "test"]
