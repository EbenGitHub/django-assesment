FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --system

COPY . /app/

EXPOSE 8000

CMD ["pipenv", "run", "start"]
