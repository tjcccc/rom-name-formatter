import os
import json
from models.config import Config


class ConfigService:
    def __init__(self, config_path):
        self.config_path = config_path

    def load_config(self):
        if not os.path.exists(self.config_path):
            self.create_config_file()
            print('No config file founded. Created a new config.')
        with open(self.config_path, 'r') as config_file:
            config_json = json.load(config_file)
            config = Config(**config_json)
        print('Config loaded.')
        return config

    def save_config(self, config: Config):
        with open(self.config_path, 'w') as config_file:
            json.dump(config, config_file, indent=2, default=vars)
        print('Config saved.')

    def create_config_file(self):
        config = Config()
        self.save_config(config)
