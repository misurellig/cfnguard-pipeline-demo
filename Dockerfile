FROM ubuntu:latest

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && \
    apt-get install build-essential -y && \
    apt-get install curl -y && \
    apt-get install cargo -y && \
    apt-get install git -y

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN curl -kLO https://github.com/aws-cloudformation/cloudformation-guard/releases/download/1.0.0/cfn-guard-linux-1.0.0.tar.gz

RUN tar xvf cfn-guard-linux-1.0.0.tar.gz . && \
    ln -s /cfn-guard-linux/cfn-guard /usr/local/bin/cfn-guard