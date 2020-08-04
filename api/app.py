from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from api import config, routes
from api.models import db, ma
from flask_cors import CORS


app = Flask(__name__)
app.debug = config.DEBUG

app.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# enable CORS
CORS(app)

db.init_app(app)
db.app = app
ma.init_app(app)



for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)


if __name__ == '__main__':
	server.run(host=config.HOST, port=config.PORT)
