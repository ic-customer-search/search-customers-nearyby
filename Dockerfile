FROM python:3.7.3-alpine

WORKDIR /app
COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY app .

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh


ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "main.py"]
