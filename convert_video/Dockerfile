FROM python:3-alpine

WORKDIR /app
COPY ./create_rgb_txt.py ./create_rgb_txt.py

ENV IMAGE_EXTENSION=.jpg
ENV FPS=30

ENTRYPOINT python create_rgb_txt.py /app/input /app/output.txt "${FPS}" "${IMAGE_EXTENSION}"
