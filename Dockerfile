FROM python:3.7.3-alpine
WORKDIR /app
COPY app .

RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh


ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["python", "search_customers.py"]
