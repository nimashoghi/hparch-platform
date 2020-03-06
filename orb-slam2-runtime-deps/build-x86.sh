#!/bin/bash

docker build --rm --build-arg BASE="ubuntu:xenial" -f "./Dockerfile" -t "nimashoghi/ubuntu-xenial-orb-slam2-runtime-deps:latest" "./"
