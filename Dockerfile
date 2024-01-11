FROM python:3.9.5-slim-buster
WORKDIR / app
COPY . / app


RUN pip install -r requirements.txt
RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y


EXPOSE $PORT
CMD ["python3", "app.py"]