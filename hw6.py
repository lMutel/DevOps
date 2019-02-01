import docker

docker_im = "centos:latest"

client = docker.from_env()
print(client.images.list())