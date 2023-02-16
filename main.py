from flask import Flask
from flask_restx import Api

from config import Config

from setup_db import db
from utils import create_data
from views.genres import genres_ns
from views.directors import directors_ns
from views.movies import movies_ns


def create_app(config: Config):
    """создание приложения Flask"""
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application):
    """конфигурирование приложения"""
    db.init_app(application)

    api = Api(application)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)



if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)

    configure_app(app)
    create_data()  # функция создания и наполнения базы данных
    app.run()