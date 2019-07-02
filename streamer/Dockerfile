FROM arm32v7/ubuntu

RUN apt-get update \
    && apt-get install --yes git-core cmake libjpeg8-dev gcc g++

WORKDIR /app

RUN git clone https://github.com/jacksonliam/mjpg-streamer.git \
    && cd mjpg-streamer/mjpg-streamer-experimental \
    && make \
    && make install

WORKDIR /app/mjpg-streamer/mjpg-streamer-experimental

ENV LD_LIBRARY_PATH=.

ENTRYPOINT ["mjpg-streamer"]
