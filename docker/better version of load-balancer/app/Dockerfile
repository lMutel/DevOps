#using apache for creating a page
FROM httpd:2.4

ARG name
ARG number

RUN rm -rf /usr/local/apache2/htdocs/
COPY index.html /usr/local/apache2/htdocs/
RUN echo "                          \
<html>                              \
  <head>                            \
    <title> LoadBalancer </title>   \
  </head>                           \
  <body>                            \
    <h1>                            \
    Welcome to $name                \
    </h1>                           \
    <h2>                            \
    Current Port: 808$number        \
    </h2>                           \
  </body>                           \
</html>                             \
" >> /usr/local/apache2/htdocs/index.html