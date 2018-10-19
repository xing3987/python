From python:3.6
MAINTAINER chenxing
ENV REFRESHED_AT 2018-10-18
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
EXPOSE 7070
EXPOSE 80
CMD python proxy.py
