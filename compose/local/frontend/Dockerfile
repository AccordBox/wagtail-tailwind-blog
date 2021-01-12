FROM node:12-stretch-slim

WORKDIR /app/frontend

COPY ./frontend/package.json /app/frontend
COPY ./frontend/package-lock.json /app/frontend

ENV PATH ./node_modules/.bin/:$PATH

RUN npm install
