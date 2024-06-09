FROM python:latest
RUN apt-get install zbar-tools, tesseract-ocr && pip3 install -r requirements.txt
EXPOSE 5000
CMD flask run