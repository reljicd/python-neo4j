# Python Neo4j

## About 

Generalized projects for Neo4j GRM in Python

## Prerequisites

[Optional] Install virtual environment:

```bash
$> sudo apt install python3-pip
$> pip3 install virtualenv
$> python3 -m virtualenv venv
```

Activate virtual environment:

On macOS and Linux:
```bash
$> source venv/bin/activate
```

On Windows:
```bash
$> .\venv\Scripts\activate
```

[Optional] Install dependencies (in a new virtual environment):
```bash
$> pip install -r requirements.txt
```

Add project directory to PYTHONPATH
```bash
$> export PYTHONPATH=$PYTHONPATH:$(pwd)
```

## Configuration parameters

Configuration parameters are passed through environment variables:

* **GRAPH_DB_HOST** - Graph host. Defaults to **localhost**.

* **GRAPH_DB_PORT** - Graph port. Defaults to **27017**.

* **GRAPH_DB** - Graph db to use. Defaults to **graph_db**.

## How to run

### Default

```bash
$> python ${SERVICE_NAME} ${METHOD_NAME} [parameters...]
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/activate_venv_and_run_python.sh
$> scripts/activate_venv_and_run_python.sh ${SERVICE_NAME} ${METHOD_NAME} [parameters...]
```

### Docker

It is possible to run application using Docker:

Build Docker image:
```bash
$> docker build -t python_neo4j -f docker/Dockerfile .
```

Run Docker container:
```bash
$> docker run --rm -t \
        -e GRAPH_DB_HOST=${GRAPH_DB_HOST} \
        -e GRAPH_DB_PORT=${GRAPH_DB_PORT} \
        -e GRAPH_DB=${GRAPH_DB} \
       python_neo4j ${SERVICE_NAME} ${METHOD_NAME} [parameters...]
```

#### Docker helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/run_docker.sh
$> scripts/run_docker.sh ${SERVICE_NAME} ${METHOD_NAME} [parameters...]
```

## Tests

### Default

```bash
$> python -m pytest tests
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/activate_venv_and_run_python.sh
$> scripts/activate_venv_and_run_python.sh -m pytest tests
```

#### PyCharm

- You can run individual tests from PyCharm by simply right-clicking a test file, and choosing "Run 'pytest in ...''".
- A test may not work yet on the first try, because the Working directory needs to be adjusted. Go to `Run > Edit Configurations...`. Now select the corresponding run configuration, and set the `Working directory` field to the root directory of the python-neo4j project. 


### Docker

It is possible to run application using Docker:

Build Docker image:
```bash
$> docker build -t python_neo4j -f docker/Dockerfile .
```

Run Docker container, and specify GraphDB credentials:
```bash
$> docker run --rm -t \
        -e GRAPH_DB_HOST=${GRAPH_DB_HOST} \
        -e GRAPH_DB_PORT=${GRAPH_DB_PORT} \
        -e GRAPH_DB=${GRAPH_DB} \
       python_neo4j -m pytest /tests
```

#### Docker helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/run_docker.sh
$> scripts/run_docker.sh -m pytest /tests
```

### Docker Compose

It is possible to run application using Docker Compose which includes **python-neo4j**:

Build Docker Compose images:
```bash
$> docker-compose -f docker/docker-compose.yml build
```

Run Docker Compose containers:
```bash
$> docker-compose -f docker/docker-compose.yml run --rm \
       --name ${CONTAINER_NAME} \
       ${CONTAINER_NAME} -m pytest /tests
```

#### Docker Compose helper script

It is possible to run all of the above with helper script:

```bash
$> chmod +x scripts/run_docker.sh
$> scripts/run_tests_using_docker_compose.sh
```
