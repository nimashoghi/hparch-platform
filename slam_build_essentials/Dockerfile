FROM arm32v7/ubuntu:xenial

WORKDIR /root

# install dependencies
RUN apt-get update && \
    apt-get install --yes wget unzip cmake git build-essential pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libtbb-dev libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libgtk2.0-dev libatlas-base-dev libeigen3-dev libblas-dev liblapack-dev libglew-dev gfortran python2.7-dev python3-dev python-numpy python3-numpy

# install Ninja
RUN wget https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-linux.zip \
    && unzip ninja-linux.zip -d /usr/local/bin/ \
    && update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force

# install OpenCV
WORKDIR /root
RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip \
    && unzip opencv.zip \
    && cd opencv-3.1.0/ \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. \
    && make -j4 \
    && make install

# install Pangolin
WORKDIR /root
RUN git clone https://github.com/stevenlovegrove/Pangolin \
    && cd Pangolin \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE .. \
    && make -j4 \
    && make install
