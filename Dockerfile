FROM python:3.9.7

COPY . /app/

RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial main" >>/etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main" >>/etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial universe" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial universe" >>/etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates universe" >>/etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main" >>/etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe" >>/etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security universe" >>/etc/apt/sources.list

RUN apt-get -y update \
    && apt-get -y install gcc python3.9-dev flex bison phantomjs unzip vim git supervisor

WORKDIR /app

RUN cd /app  \
    && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["gunicorn", "-c", "gunicorn.conf.py", "run:app"]

EXPOSE 8080


