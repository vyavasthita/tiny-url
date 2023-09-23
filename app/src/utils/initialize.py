import os
from typing import Annotated
from fastapi import Depends
from cassandra.cluster import Session
from ..dependencies.config_dependency import Config
from ..dependencies.db_dependency import get_db


def create_log_directory():
    base_dir = os.path.abspath(os.path.dirname(__name__))

    if not os.path.exists(os.path.join(base_dir, Config().LOGS_DIR)):
        os.mkdir(os.path.join(base_dir, Config().LOGS_DIR))


def initialize():
    create_log_directory()
