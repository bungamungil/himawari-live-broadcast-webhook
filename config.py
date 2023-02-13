import json
import os.path
from errors import ConfigNotFound

CONFIG_FILE = "config.json"


def read_config():
    if os.path.isfile(CONFIG_FILE):
        config_file = open(CONFIG_FILE)
        config_json = json.load(config_file)
        config_file.close()
        return config_json
    else:
        raise ConfigNotFound
