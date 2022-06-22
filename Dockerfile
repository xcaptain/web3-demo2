FROM python:3-buster

WORKDIR /app
COPY . .
RUN pip install requests
RUN pip install web3

CMD ["python", "main.py"]