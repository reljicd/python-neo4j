from str2bool import str2bool

from python_neo4j.utils.env_vars import get_env

NEO4J_HOST: str = get_env(
    key='NEO4J_HOST',
    default='localhost')
NEO4J_PORT: int = int(get_env(
    key='NEO4J_PORT',
    default='7687'))
NEO4J_USERNAME: str = get_env(
    key='NEO4J_USERNAME',
    default='neo4j')
NEO4J_PASSWORD: str = get_env(
    key='NEO4J_PASSWORD',
    default='s3cr3t')
NEO4J_DATABASE: str = get_env(
    key='NEO4J_DATABASE',
    default='graph_db')

LOGGING_LEVEL: str = get_env(key='LOGGING_LEVEL', default='info')

DEBUG: bool = str2bool(get_env(key='DEBUG', default='False'))
