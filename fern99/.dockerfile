FROM python:3.11-slim

WORKDIR /fern99

COPY . . 

RUN pip install django

RUN python manage.py migrate


EXPOSE 9999

CMD ["python","manage.py",["runsvever"],"0.0.0.0:9999"]

