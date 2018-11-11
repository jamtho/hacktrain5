FROM arm32v7/ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

COPY . /app

RUN apt-get -y update

RUN apt-get install -y python python-pip

RUN apt-get install -y pm-utils libusb-1.0-0 libudev-dev

RUN su -c "dpkg -i /app/brickd_linux_latest_armhf.deb"

RUN pip install tinkerforge
RUN pip install requests
    
EXPOSE 4223 8088 8457

ENV WEB_LISTEN_PORT 8088

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
