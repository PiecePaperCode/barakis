FROM python:3.9

WORKDIR app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ogame-8.1.0.21.tar.gz .
RUN pip install ogame-8.1.0.21.tar.gz

COPY src/ .

EXPOSE 80

CMD ["python", "-u", "main.py"]
