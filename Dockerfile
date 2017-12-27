FROM debian
ADD . /opt/latex
WORKDIR /opt/latex
RUN apt-get update
RUN apt-get -y install texlive-full python3 python3-pip
RUN pip3 install -r requirements.txt
CMD ["rq", "worker", "-c", "settings"]
