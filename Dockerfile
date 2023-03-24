FROM python:3.12.0a6-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python3", "app.py"]