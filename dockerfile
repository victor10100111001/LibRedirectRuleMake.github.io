FROM python:3.10

RUN pip install json requests urllib.parse bs4 re colorama socket subprocess locale operator flask

WORKDIR /app

EXPOSE 443 80

CMD [ "python", "./server.py" ]