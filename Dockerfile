FROM centos:latest
MAINTAINER Kalyan Penmetsa "penmetsa29@gmail.com"
RUN yum update -y
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u python-pip
RUN pip install --upgrade pip
EXPOSE 5000
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["src/main.py"]