#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "No input parameters supplied"
    exit 1
fi

IMAGE_NAME=python-neo4j
echo -e "\nSet docker image name as ${IMAGE_NAME}\n"

echo -e "\nDocker build image with name ${IMAGE_NAME}...\n"
docker build -t ${IMAGE_NAME} -f docker/Dockerfile .

CONTAINER_NAME=${IMAGE_NAME}

echo -e "\nStop running Docker containers with container name ${CONTAINER_NAME}...\n"
docker stop "$(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')"

echo -e "\nStart Docker container of the image ${IMAGE_NAME} with name ${CONTAINER_NAME}...\n"
docker run --rm -t \
    -e GRAPH_DB_HOST="${GRAPH_DB_HOST}" \
    -e GRAPH_DB_PORT="${GRAPH_DB_PORT}" \
    -e GRAPH_DB="${GRAPH_DB}" \
    ${IMAGE_NAME} "$@"