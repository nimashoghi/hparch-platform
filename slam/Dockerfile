FROM nimashoghi/slam_build_essentials:latest

# install ORB_SLAM2
WORKDIR /root
RUN git clone https://github.com/raulmur/ORB_SLAM2 \
    && cd ORB_SLAM2 \
    && chmod +x ./build.sh \
    && ./build.sh

WORKDIR /root

ENTRYPOINT ["/root/ORB_SLAM2/Examples/Monocular/mono_tum", "/root/ORB_SLAM2/Vocabulary/ORBvoc.txt", "/data/settings.yaml", "/data"]
