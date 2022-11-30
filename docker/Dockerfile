FROM python:3.7

ENV APP_HOME /app
ENV TESTS_PATH /app/tests
ENV PYTHONPATH ${PYTHONPATH}:${APP_HOME}:${TESTS_PATH}

WORKDIR ${APP_HOME}

COPY ./python-neo4j/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./python-neo4j ${APP_HOME}

ENTRYPOINT ["python"]
