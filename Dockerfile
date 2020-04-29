
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -yq \
    python3-pygame
ENV DEBIAN_FRONTEND teletype

RUN useradd --uid 1000 -ms /bin/bash user

WORKDIR /home/user

ADD demos .

RUN chown -R user .

USER user

ENTRYPOINT [ "python3" , "-u", "./hello_world/boot.py" ]
