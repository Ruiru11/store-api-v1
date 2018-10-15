from flask import Flask

from .config import Config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config_by_name[config_name])
    return app
