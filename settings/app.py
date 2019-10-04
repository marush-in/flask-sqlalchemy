from flask import Flask

from settings.database import init_db


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.config.Config')

    init_db(app)

    return app


app = create_app()
