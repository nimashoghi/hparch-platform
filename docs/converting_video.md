# Converting video to image sequence using ffmpeg (Docker)

`docker run -v {{video path}}:/app/video.{{video extension}} -v {{output image path}}:/app/images jrottenberg/ffmpeg -i /app/video.{{video extension}} -vf fps={{video fps}} /app/images/%04d.jpg -hide_banner`

# Creating `rgb.txt` from image sequence

`python create_rgb_txt.py <input image sequence> <output rgb.txt path> <fps> [image file extension]`

## From Docker

`docker run -it -v <input image sequence>:/app/input -v <output rgb.txt path>:/app/output.txt -e "IMAGE_EXTENSION=.<image file extension>" -e "FPS=<FPS>" nimashoghi/convert_video`
