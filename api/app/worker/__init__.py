from flask import Blueprint
from flask_restful import Api

from .routes import GetReposFromGithubResources, AllReposResources, GetRepoResources

worker = Blueprint('worker', __name__)
worker_api = Api(worker)

worker_api.add_resource(GetReposFromGithubResources,
                        '/repo')  # this take one argument '/repo?name=...', where should be name of repo on Github
worker_api.add_resource(AllReposResources, '/repos')  # this endpoint takes no arguments
worker_api.add_resource(GetRepoResources,
                        '/id')  # this take one argument '/id?repo_id=...', where should be repo_id (from github)
