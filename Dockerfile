FROM python:3
WORKDIR /usr/src/app

RUN pip install pandas, time

COPY . .

CMD ["python", "./app.py"]
