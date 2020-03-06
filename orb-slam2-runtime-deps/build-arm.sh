#!/bin/bash

docker build --rm --build-arg BASE="arm32v7/ubuntu:xenial" -f "./Dockerfile" -t "nimashoghi/arm32v7-ubuntu-xenial-orb-slam2-runtime-deps:latest" "./"
