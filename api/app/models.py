from db import db


class ReposInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    repo_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String, nullable=False)
    html_url = db.Column(db.String)
    description = db.Column(db.String)
    private = db.Column(db.String, default=False, nullable=False)
    created_at = db.Column(db.TIMESTAMP)
    watchers = db.Column(db.String)

    def __init__(self, repo_id, name, html_url, description, private, created_at, watchers):
        self.repo_id = repo_id
        self.name = name
        self.html_url = html_url
        self.description = description
        self.private = private
        self.created_at = created_at
        self.watchers = watchers

    def serialize(self):
        return {
            'repo_id': self.repo_id,
            'name': self.name,
            'description': self.description,
            'private': self.private,
            'created_at': self.created_at,
            'watchers': self.watchers,
        }
