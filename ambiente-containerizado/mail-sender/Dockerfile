FROM python:3.8.1-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
CMD ["flask","run","--host=0.0.0.0"]