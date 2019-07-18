#!/bin/bash

docker-compose up -d slam_dev
docker-compose exec -it --privileged slam_dev /bin/bash
