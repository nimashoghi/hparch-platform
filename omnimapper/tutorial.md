# Running LSD_SLAM with Sample Dataset

## Using Docker and Docker Compose

1. Make sure you have Docker and Docker Compose installed. Visit [the following link](https://docs.docker.com/install/) for more information.
2. Make sure you have an XServer server running on your computer. Make sure to disable all kinds of authentication and access control measures.
3. Clone this repository and navigate to the `omnimapper` directory.
4. Change line 6 in the docker-compose.yml file to match `- DISPLAY={YOUR_IP}:0.0`. You can get your local ip address on Windows using `ipconfig` and on Ubuntu using `ifconfig`.
5. Run `docker-compose up -d`
6. Once the Docker container starts, find its id using `docker ps`. Then, run the following command to start a bash instance in the container: `docker exec -it {CONTAINER_ID} /bin/bash`.
7. In your instance, download and extract the sample data using the following command: `apt-get install --yes unzip && wget http://vmcremers8.informatik.tu-muenchen.de/lsd/LSD_room.bag.zip && unzip LSD_room.bag.zip`.
8. Then, run the following commands, in the given order, in separate bash instances (you can create new ones using the same method you used in step 6):
    1. `rosrun lsd_slam_viewer viewer`
    2. `rosrun lsd_slam_core live_slam image:=/image_raw camera_info:=/camera_info`
    3. `rosbag play ~/LSD_room.bag`
9. Finally, you should see a window like the following: ![screenshot](https://i.imgur.com/YdU5gSs.png)
