FROM node:12-stretch-slim as frontend-builder

WORKDIR /app/frontend

COPY ./frontend/package.json /app/frontend
COPY ./frontend/package-lock.json /app/frontend

ENV PATH ./node_modules/.bin/:$PATH

RUN npm install

COPY ./frontend .

RUN npm run build

################################################################################
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN addgroup --system django \
    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./compose/production/web/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/web/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
RUN chown django /start

WORKDIR /app

# avoid 'permission denied' error
RUN mkdir /app/static
RUN mkdir /app/media

# copy project code
COPY . .
COPY --from=frontend-builder /app/frontend/build /app/frontend/build

RUN chown -R django:django /app

USER django

ENTRYPOINT ["/entrypoint"]
