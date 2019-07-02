# Live Stream Raspberry Pi Camera Video Across the Network

#### Run the `streamer` image with the `output_http` output plugin.

`docker run -t -i --privileged -p 8080:8080 nimashoghi/streamer -i 'input_uvc.so --resolution 1280x720 --device /dev/video0' -o output_http.so`

Make sure to change `1280x720` and `/dev/video0` to reflect your video resolution and Linux device file path, respectively.

#### Visit the URL `http://{RASPBERRY_PI_LOCAL_IP}:8080/?action=stream` in your browser

# Add preference option for record directory
