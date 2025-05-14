FROM python:3.13-slim

RUN pip install flask

RUN useradd -m -s /bin/bash flaskuser
USER flaskuser

WORKDIR /home/flaskuser/app
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]