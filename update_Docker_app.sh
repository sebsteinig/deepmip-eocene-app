#!/bin/bash

# Check if image name is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <image_name>"
    exit 1
fi

# Get the image name from the command-line argument
image_name="$1"

# Get the container ID based on the image name
container_id=$(sudo docker ps -a --filter "ancestor=$image_name" --format "{{.ID}}")

# Check if a container ID was found
if [ -z "$container_id" ]; then
    echo "No container found for image: $image_name"
    exit 1
fi

# Stop the container
sudo docker stop "$container_id"

# Remove the container
sudo docker rm "$container_id"

echo "Container $container_id stopped and removed successfully."

# Remove the image
sudo docker rmi "$image_name"

echo "Image $image_name removed successfully."

# Pull the updated image
sudo docker pull "$image_name"

echo "Image $image_name pulled successfully."

# Launch the updated container
sudo docker run -p 8501:8501 $image_name
