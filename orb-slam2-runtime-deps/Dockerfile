ARG BASE
FROM ${BASE}

# install dependencies
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    ca-certificates wget unzip cmake git build-essential pkg-config \
    libjpeg-dev libtiff5-dev libjasper-dev libpng-dev \
    libtbb-dev libavcodec-dev libavformat-dev libswscale-dev \
    libxvidcore-dev libx264-dev libgtk2.0-dev libatlas-base-dev \
    libeigen3-dev libblas-dev liblapack-dev libglew-dev gfortran \
    python2.7-dev python3-dev python-numpy python3-numpy

# install OpenCV
WORKDIR /build/opencv
RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.4.0.zip \
    && unzip opencv.zip \
    && cd opencv-3.4.0/ \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_CUDA=ON -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF .. \
    && make -j \
    && make install

# install Pangolin
WORKDIR /build/Pangolin
RUN git clone https://github.com/stevenlovegrove/Pangolin \
    && cd Pangolin \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j \
    && make install

COPY ./Thirdparty/ /build

# install DBoW2
WORKDIR /build/DBoW2
RUN mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j \
    && make install

# install g2o
WORKDIR /build/g2o
RUN mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j \
    && make install

# install fmtlib
WORKDIR /build/fmt
RUN wget https://github.com/fmtlib/fmt/releases/download/5.3.0/fmt-5.3.0.zip \
    && unzip fmt-5.3.0.zip \
    && cd fmt-5.3.0 \
    && mkdir build \
    && cd build \
    && cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local .. \
    && make \
    && make install

RUN rm -rf /build
