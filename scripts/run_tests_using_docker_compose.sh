#!/usr/bin/env bash

export CONTAINER_NAME=python-neo4j
echo -e "\nSet docker container name as ${CONTAINER_NAME}\n"

stop_and_delete_containers () {
    echo -e "\nStop running Docker containers with container name ${CONTAINER_NAME}...\n"
    docker stop "$(docker ps -a | grep ${CONTAINER_NAME} | awk '{print $1}')" 2>/dev/null

    echo -e "\nStop and delete Neo4j containers... \n"
    docker stop "$(docker ps -a | grep neo4j | awk '{print $1}')" 2>/dev/null
    docker rm "$(docker ps -a | grep neo4j | awk '{print $1}')" 2>/dev/null

}

stop_and_delete_containers

docker-compose -f docker/docker-compose-tests.yml build

echo -e "\nStart Docker Compose...\n"
docker-compose -f docker/docker-compose-tests.yml run --rm \
    --name ${CONTAINER_NAME} \
    ${CONTAINER_NAME} -m pytest /app/tests

stop_and_delete_containers