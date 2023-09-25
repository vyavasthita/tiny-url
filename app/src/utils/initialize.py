import os
from ..dependencies.config_dependency import Config


def create_log_directory():
    base_dir = os.path.abspath(os.path.dirname(__name__))

    if not os.path.exists(os.path.join(base_dir, Config().LOGS_DIR)):
        os.mkdir(os.path.join(base_dir, Config().LOGS_DIR))


def initialize():
    create_log_directory()
