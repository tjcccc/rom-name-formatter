import os
import json
from models.config import Config


def create_config_file(config_path):
    config = Config(
        roms_directory='',
        saves_directory='',
        states_directory='',
        tags=[],
        name_format=''
    )
    save_config(config, config_path)


def load_config(config_json_path):
    if not os.path.exists(config_json_path):
        create_config_file(config_json_path)
    with open(config_json_path, 'r') as config_file:
        config_json = json.load(config_file)
        config = Config(**config_json)
    return config


def save_config(config: Config, config_json_path):
    with open(config_json_path, 'w') as config_file:
        json.dump(config, config_file, indent=2, default=vars)
