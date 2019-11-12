import os


class Config:
    SECRET_KEY = 'very_secret_key'


class TestConfig:
    SECRET_KEY = 'test_secret_key'


class ProductionConfig:
    SECRET_KEY = 'prod_secret_key'


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProductionConfig
    else:
        return Config

