#uding nginx for creating a balancer
FROM nginx:alpine

#nginx configuration
RUN rm /etc/nginx/conf.d/*
COPY proxy.conf /etc/nginx/conf.d/