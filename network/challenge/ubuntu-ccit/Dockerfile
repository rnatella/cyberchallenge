FROM ubuntu:18.04

ARG PKGS
ARG SCRIPTS
ARG EXEC

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y openssh-server iproute2 iptables inetutils-ping vim nano net-tools dnsutils python3-scapy python3-flask traceroute $PKGS

## ssh ##

RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# exec
RUN eval ${EXEC}

# bin
COPY bin/level* /usr/local/bin/
COPY bashrc /root/.bashrc

# entrypoint
COPY entrypoint.sh /usr/local/bin/
RUN sed -i -- "s^# startup scripts^${SCRIPTS}^g" /usr/local/bin/entrypoint.sh

ENTRYPOINT /usr/local/bin/entrypoint.sh
