FROM ubuntu:xenial
# FROM arm32v7/ubuntu:xenial

WORKDIR /root

# install dependencies
RUN apt-get update && \
    apt-get install --yes wget unzip cmake git build-essential pkg-config ffmpeg libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libtbb-dev libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libgtk2.0-dev libatlas-base-dev libeigen3-dev libblas-dev liblapack-dev libglew-dev gfortran python2.7-dev python3-dev python-numpy python3-numpy

ENV FFMPEG_PATH='/usr/bin/ffmpeg' \
    FFPROBE_PATH='/usr/bin/ffprobe'


# install Ninja
RUN wget https://github.com/ninja-build/ninja/releases/download/v1.9.0/ninja-linux.zip \
    && unzip ninja-linux.zip -d /usr/local/bin/ \
    && update-alternatives --install /usr/bin/ninja ninja /usr/local/bin/ninja 1 --force

ARG OPENCV_MAKE_FLAGS="-D CMAKE_BUILD_TYPE=RELEASE \
    -D BUILD_DOCS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_JAVA=OFF \
    -D BUILD_opencv_apps=OFF \
    -D BUILD_opencv_aruco=OFF \
    -D BUILD_opencv_bgsegm=OFF \
    -D BUILD_opencv_bioinspired=OFF \
    -D BUILD_opencv_ccalib=OFF \
    -D BUILD_opencv_datasets=OFF \
    -D BUILD_opencv_dnn_objdetect=OFF \
    -D BUILD_opencv_dpm=OFF \
    -D BUILD_opencv_fuzzy=OFF \
    -D BUILD_opencv_hfs=OFF \
    -D BUILD_opencv_java_bindings_generator=OFF \
    -D BUILD_opencv_js=OFF \
    -D BUILD_opencv_img_hash=OFF \
    -D BUILD_opencv_line_descriptor=OFF \
    -D BUILD_opencv_optflow=OFF \
    -D BUILD_opencv_phase_unwrapping=OFF \
    -D BUILD_opencv_python3=OFF \
    -D BUILD_opencv_python_bindings_generator=OFF \
    -D BUILD_opencv_reg=OFF \
    -D BUILD_opencv_rgbd=OFF \
    -D BUILD_opencv_saliency=OFF \
    -D BUILD_opencv_shape=OFF \
    -D BUILD_opencv_stereo=OFF \
    -D BUILD_opencv_stitching=OFF \
    -D BUILD_opencv_structured_light=OFF \
    -D BUILD_opencv_superres=OFF \
    -D BUILD_opencv_surface_matching=OFF \
    -D BUILD_opencv_ts=OFF \
    -D BUILD_opencv_xobjdetect=OFF \
    -D BUILD_opencv_xphoto=OFF \
    -D BUILD_SHARED_LIBS=ON \
    -D WITH_TBB=ON \
    -D WITH_OPENMP=ON \
    -D WITH_OPENCL=ON \
    -D WITH_CUDA=ON \
    -D WITH_GTK=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D WITH_V4L=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D WITH_QT=ON \
    -D WITH_OPENGL=ON \
    -D BUILD_JPEG=ON \
    -D BUILD_PNG=ON \
    -D BUILD_JASPER=ON \
    -D BUILD_ZLIB=ON \
    -D WITH_JPEG=ON \
    -D WITH_PNG=ON \
    -D WITH_JASPER=ON \
    -D WITH_ZLIB=ON \
    -D WITH_OPENEXR=OFF \
    -D CMAKE_INSTALL_PREFIX=$LIB_PREFIX \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules"

# install OpenCV
WORKDIR /root
RUN wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip \
    && unzip opencv.zip \
    && cd opencv-3.1.0/ \
    && mkdir build \
    && cd build \
    && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local  .. \
    && make -j4 \
    && make install

# install Pangolin
WORKDIR /root
RUN git clone https://github.com/stevenlovegrove/Pangolin \
    && cd Pangolin \
    && mkdir build \
    && cd build \
    && cmake ${OPENCV_MAKE_FLAGS} .. \
    && make -j4 \
    && make install
