#!/bin/bash

docker build --rm --build-arg BASE="openhorizon/aarch64-tx2-cudabase" -f "./Dockerfile" -t "nimashoghi/ubuntu-xenial-jetson-orb-slam2-runtime-deps:latest" "./"
