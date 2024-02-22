
# Docker-demo

A simple project to get started with Docker.

## Play with Docker

For interactive Docker sessions, you can use [Play with Docker](https://labs.play-with-docker.com/).

## Project Setup

### Step 1: Create Empty Files

Create empty files for your Docker project:

```bash
touch Dockerfile
touch app.py
touch requirements.txt
```

### Step 2: Copy File Contents to Host

Now, add the content to `Dockerfile`, `app.py`, and `requirements.txt` on your local machine.

### Step 3: Build Docker Image

Build the Docker image for your Python web app:

```bash
docker build -t my-python-web-app .
```

### Step 4: Create Container from Image

Run a Docker container from the created image:

```bash
docker run -p 5000:5000 my-python-web-app
```

Your Flask web application will be accessible at [http://localhost:5000/](http://localhost:5000/).


Creating your own Docker image and uploading it to Docker Hub involves several steps. Here's a step-by-step guide:


### Step 5: Build the Docker Image to push on Docker Hub
Open a terminal or command prompt in the directory where your Dockerfile is located and run the following command:

```bash
docker build -t maheshdhage24/my-python-web-app:v1 
```

Replace `your-username`, `your-image-name`, and `tag` with your Docker Hub username, desired image name, and a version tag, respectively.

### Step 6: Verify the Image
Ensure that the image has been successfully built by running:

```bash
docker images
```

You should see your newly created image in the list.

### Step 7: Log in to Docker Hub
Before you can push your image to Docker Hub, you need to log in. Run the following command and enter your Docker Hub credentials when prompted:

```bash
docker login
```

### Step 7: Push the Image to Docker Hub
Push your image to Docker Hub using the following command:

```bash
docker push maheshdhage24/my-python-web-app:v1
```

### Step 8: Verify on Docker Hub
Visit [Docker Hub](https://hub.docker.com/), log in with your credentials, and you should see your uploaded image in your repository.

Your Docker image is now available on Docker Hub and can be pulled by others or used in your deployments. Ensure that your Docker Hub repository is set to public if you want others to access it without authentication.




### Step 9: Stop All Running Containers

Stop all running Docker containers:

```bash
docker stop $(docker ps -a -q)
```

### Step 10: Remove All Containers

Remove all Docker containers:

```bash
docker rm $(docker ps -a -q)
```

### Step 11: Remove All Images

Remove all Docker images:

```bash
docker rmi $(docker images -q)
```
