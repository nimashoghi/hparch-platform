# This worked

https://www.feeditout.com/raspberry-pi-3-csi-camera-motion-devvideo0/

## Instead of using the driver in there, we can use the streamer package and pipe the http video stream into motion

http://www.lavrsen.dk/foswiki/bin/view/Motion/MjpgStreamer

# Other guides (didn't work for me)

https://www.raspberrypi.org/forums/viewtopic.php?p=498901&sid=6037d26b8314abedef6fb75d93da9daf#p498901

# Setting FPS:

`sudo v4l2-ctl -p {fps}`

# Setting Resoltuion

`sudo v4l2-ctl -v width={width},height={height}`
