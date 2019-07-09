ARG SLAM_BUILD_ESSENTIALS_IMAGE=nimashoghi/slam_build_essentials
ARG SLAM_BUILD_ESSENTIALS_VERSION
FROM ${SLAM_BUILD_ESSENTIALS_IMAGE}:${SLAM_BUILD_ESSENTIALS_VERSION}

# install dependencies
RUN apt-get update && \
    apt-get install --yes cmake

WORKDIR /app
COPY . .

RUN mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release .. \
    && make

WORKDIR /app/build

CMD ./calibration /app/assets/config.xml
