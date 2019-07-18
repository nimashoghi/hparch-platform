@echo off

docker-compose up -d slam_dev
docker-compose exec --privileged slam_dev /bin/bash
