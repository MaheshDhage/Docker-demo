# Docker-demo
Just play with docker

https://labs.play-with-docker.com/
touch Dockerfile
ls
click on editor
touch Dockerfile
touch app.py
touch requirements.txt
ls
docker build -t my-python-web-app .
docker run -p 5000:5000 my-python-web-app

# Stop all running containers
docker stop $(docker ps -a -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Remove all images
docker rmi $(docker images -q)
