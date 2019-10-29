import logging

from app import app
from config import Config
from create_db import create_db
from db import db
from worker import worker


def run_app():
    app.config.from_object(Config)
    app.register_blueprint(create_db)
    app.register_blueprint(worker)

    db.init_app(app)

    logging.basicConfig(level=logging.DEBUG)
    logging.info('App has been started')

    return app


if __name__ == '__main__':
    run_app().run(debug=True, host='0.0.0.0')
