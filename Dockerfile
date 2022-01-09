FROM python:3.8.10-slim-buster

ENV NOIP_USERNAME ""
ENV NOIP_PASSWORD ""
ENV NOIP_HOSTNAME ""
ENV NOIP_INTERVAL 300

WORKDIR /prj

RUN useradd -m -r user && \
    chown user /prj


COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

USER user


ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}

CMD ["python", "-u", "app.py"]
