FROM python:3.7

LABEL maintainer="alskarf@gmail.com"

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "__init__.py" ]