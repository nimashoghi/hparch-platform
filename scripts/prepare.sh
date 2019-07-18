# Make sure to have SSH enabled.

# Setting up dependencies
sudo apt-get update && sudo apt-get upgrade && sudo apt-get install --yes build-essential curl libssl-dev libffi-dev python3-pip

# Docker
curl -sL get.docker.com | sed 's/9)/10)/' | sudo sh
sudo usermod -aG docker pi

# Docker-Compose
sudo pip3 install docker-compose
