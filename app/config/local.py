"""
Local and Testing configuration
"""

from .base import BaseConfig


class LocalConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/dairy_manager'

