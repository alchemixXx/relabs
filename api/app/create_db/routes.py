import logging

from flask_restful import Resource

from db import db


class CreateDB(Resource):
    def post(self):
        try:
            db.create_all()
            db.session.commit()
            logging.info('DB has been created')
        except Exception as e:
            logging.error(f"Something went wrong, DB creation failed. Error: {e}")
        return 'ok'
