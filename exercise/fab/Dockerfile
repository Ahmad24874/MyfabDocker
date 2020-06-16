FROM python:3.7.7

WORKDIR /home/work

COPY requirements.txt /home/work

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install vim -y

RUN flask fab create-app --name myapp --engine SQLAlchemy
RUN export FLASK_APP=app
RUN cd /home/work/myapp && flask fab create-admin --username admin --firstname admin --lastname flask --email admin@flask.org --password password
RUN cp -r myapp/. ./
#RUN python testdata.py

EXPOSE 8080

CMD ["bash"]
