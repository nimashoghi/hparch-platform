#!/bin/bash

docker build --rm --build-arg BASE="nvidia/cuda:8.0-devel" -f "./Dockerfile" -t "nimashoghi/ubuntu-xenial-cuda-orb-slam2-runtime-deps:latest" "./"
