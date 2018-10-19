From python:3.6
MAINTAINER chenxing
ENV REFRESHED_AT 2018-10-19
ENV PATH /usr/local/bin:$PATH
ADD . /code
WORKDIR /code
COPY ./scrapyd.conf /etc/srapyd/
RUN pip3 install -r requirements.txt
EXPOSE 6800
CMD scrapyd