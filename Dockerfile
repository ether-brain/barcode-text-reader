FROM python:latest
RUN apt-get update
RUN apt-get install zbar-tools
RUN apt-get install tesseract-ocr
COPY srv ./
WORKDIR ./flask_app
RUN pip3 install -r requirements.txt
EXPOSE 5000
WORKDIR /srv
CMD flask run