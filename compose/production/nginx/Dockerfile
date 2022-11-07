FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/nginx/nginx.conf /etc/nginx/conf.d
