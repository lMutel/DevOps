FROM centos/7

RUN yum update \
    && yum install httpd \
    && systemctl enable httpd \
    && systemctl start httpd 
