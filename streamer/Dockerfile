FROM arm32v6/alpine

# Build dependencies
RUN apk add --no-cache --virtual .build-deps alpine-sdk cmake git jpeg-dev linux-headers raspberrypi-dev

# Runtime dependencies
RUN apk add --no-cache jpeg raspberrypi raspberrypi-libs

WORKDIR /build
RUN git clone https://github.com/jacksonliam/mjpg-streamer.git \
    && cd mjpg-streamer/mjpg-streamer-experimental \
    && make \
    && make install \
    && rm -rf /build

RUN apk del .build-deps

WORKDIR /
ENV LD_LIBRARY_PATH=/opt/vc/lib/

ENTRYPOINT ["mjpg_streamer"]
