from datetime import datetime
from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'admin',
    'host': 'localhost',
    'port': 27018
}       

db = MongoEngine()
db.init_app(app)

class Cache(db.Document):
    username = db.StringField()
    registry = db.StringField()
    data = db.StringField()
    ttl = db.IntField()
    _datetime = db.DecimalField()

    def to_json(self):
        return {
            "username": self.username,
            "registry": self.registry,
            "data": self.data,
            "ttl": self.ttl,
            "_datetime": datetime.fromtimestamp(self._datetime)
        }

@app.route('/info', methods=['GET'])
def main():
    return jsonify({"msg": "I'm working!"})

@app.route('/create_cache', methods=['POST'])
def create_cache():
    record = json.loads(request.data)
    cache = Cache(
        username=record['username'],
        registry=record['registry'],
        data=record['data'],
        _datetime=datetime.now().timestamp(),
        ttl=record['ttl']
        )
    cache.save()
    return jsonify({'msg': 'Cache created.'}), 200

@app.route('/query_all', methods=['GET'])
def query_all():
    caches = Cache.objects.all()
    return jsonify({'data': caches})