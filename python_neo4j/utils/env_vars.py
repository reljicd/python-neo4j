import configparser
import os

config_file_path = os.getenv('CONFIG_FILE')
if config_file_path:
    config = configparser.ConfigParser()
    config.read(config_file_path)
else:
    config = None


def get_env(key: str, default: str) -> str:
    """ Returns default even if env var is empty string """
    env = os.getenv(key)
    if env:
        return env

    if config and key in config['DEFAULT'] and config['DEFAULT'][key]:
        return config['DEFAULT'][key]

    return default
