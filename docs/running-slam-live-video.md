`docker run -it -v settings.yaml:/data/settings.yaml --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix nimashoghi/orb_slam2:0.0.1-live {{path to video device}}`

-   the path to video device is usually /dev/video# (e.g. /dev/video0)
-   the /tmp/.X11-unix mount can be ignored if your X11 server has disabled access control

Working cmd: `docker run -it -v /home/pi/Desktop/settings.yaml:/data/settings.yaml --privileged -e DISPLAY="192.168.0.108:0.0" nimashoghi/orb_slam2:0.0.1-live-patched`
and then `Examples/Monocular/mono_tum /root/Vocabulary/ORBvoc.txt /data/settings.yaml 0`
