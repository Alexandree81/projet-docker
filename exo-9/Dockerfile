FROM python:3.13-slim

RUN useradd -m -s /bin/bash flaskuser

USER root
RUN pip install flask

USER flaskuser
WORKDIR /home/flaskuser/app

COPY --chown=flaskuser:flaskuser app.py .

EXPOSE 5000

CMD ["python", "app.py"]