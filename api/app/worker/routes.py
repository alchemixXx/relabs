import logging

import requests
from flask import request, jsonify
from flask_restful import Resource

from db import db
from models import ReposInfo


class GetReposFromGithubResources(Resource):
    def get(self):
        args = request.args
        name_of_repo = args['name']
        logging.info(f"requested to get all repos from acc '{name_of_repo}'")
        try:
            logging.info("Send request to github")
            response = requests.get(f'https://api.github.com/orgs/{name_of_repo}/repos')
            logging.info("Response obtained. Starting to add data to DB ")
            result = response.json()
            counter = 0
            for item in result:
                logging.info(f"Create {counter} instance of repo")
                db.session.add(
                    ReposInfo(
                        repo_id=item['id'],
                        name=item['name'],
                        html_url=item['html_url'],
                        description=item['description'],
                        private=item['private'],
                        created_at=item['created_at'],
                        watchers=item['watchers_count'],
                    )
                )
                counter += 1
            logging.info(f"Commit all instances to DB")
            db.session.commit()
            return result
        except Exception as e:
            logging.error(f'Error in getting data from github. Error: {e}')
            return f'something went wrong while getting repo info from github, {e}'


class AllReposResources(Resource):
    def get(self):
        logging.info("requested to get all repos from db")
        try:
            logging.info("Getting all repos from db")
            all_repos = ReposInfo.query.all()
            return jsonify([e.serialize() for e in all_repos])
        except Exception as e:
            logging.error(f'Error in getting data from db. Error: {e}')
            return 'something went wrong while getting info from db'


class GetRepoResources(Resource):
    def get(self):
        logging.info("requested to get specific repo from db")
        try:
            args = request.args
            repo_id = args['repo_id']
            logging.info(f"Getting repo with id {repo_id} from db")
            repo = ReposInfo.query.filter(ReposInfo.repo_id == repo_id).first()
            return jsonify(repo.serialize())
        except Exception as e:
            logging.error(f'Error in getting simple record from db. Error: {e}')
            return 'something went wrong while getting simple repo info from db'
