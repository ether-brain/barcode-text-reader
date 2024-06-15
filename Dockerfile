FROM python:latest
RUN apt-get update
#RUN apt-get install -y zbar-tools
#RUN apt-get install -y tesseract-ocr
COPY ./ ./flask_app
WORKDIR ./flask_app
RUN pip3 install -r requirements.txt