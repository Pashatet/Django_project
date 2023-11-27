FROM ubuntu:latest
LABEL authors="pashatet"

ENTRYPOINT ["top", "-b"]