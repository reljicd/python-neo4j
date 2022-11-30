from neo4j import GraphDatabase, Session, basic_auth
from neomodel import config

from python_neo4j.config.env_vars import (NEO4J_DATABASE, NEO4J_HOST,
                                          NEO4J_PASSWORD,
                                          NEO4J_PORT,
                                          NEO4J_USERNAME)

URL = f"bolt://{NEO4J_HOST}:{NEO4J_PORT}"
driver = GraphDatabase.driver(URL, auth=basic_auth(NEO4J_USERNAME,
                                                   NEO4J_PASSWORD))


def db() -> Session:
    return driver.session(database=NEO4J_DATABASE)


def bootstrap_neomodel() -> None:
    config.DATABASE_URL = (f"bolt://{NEO4J_USERNAME}:{NEO4J_PASSWORD}"
                           f"@{NEO4J_HOST}:{NEO4J_PORT}")
