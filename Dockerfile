FROM python:latest
RUN apt-get install zbar, tesseract-ocr && pip3 install -r requirements.txt
EXPOSE 5000
CMD flask run