#!/usr/bin/env bash

stop_and_delete_containers () {
    echo -e "\nStop and delete Neo4j containers... \n"
    docker stop "$(docker ps -a | grep neo4j | awk '{print $1}')" 2>/dev/null
    docker rm "$(docker ps -a | grep neo4j | awk '{print $1}')" 2>/dev/null
}

stop_and_delete_containers

echo -e "\nStart Docker Compose...\n"
docker-compose -f docker/docker-compose-neo4j.yml run -d -p 7687:7687 -p 7474:7474 neo4j