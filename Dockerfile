FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ENV TOKEN="ODg3OTA1MjQ2NDQ0MTMwMzY1.GOTvWe.dsl00Y7NMGu2-dA-CHp1hnAfMIpQzN8LUGE-5c"

COPY . /app

CMD ["python3", "/app/main.py"]