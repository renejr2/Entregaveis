FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y tmux htop

RUN echo "set -g mouse on" >> /root/.tmux.conf

WORKDIR /dir1

RUN mkdir -p dir2 dir3