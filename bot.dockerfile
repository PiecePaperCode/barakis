FROM python:3.9

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/alaingilbert/pyogame.git@develop

COPY src/ .

EXPOSE 80

CMD ["python", "-u", "main.py"]
