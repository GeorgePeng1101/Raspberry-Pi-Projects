FROM python:2
ADD . /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD ["python","ethmon.py"]
