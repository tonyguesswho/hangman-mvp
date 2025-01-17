from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

import config
from models import db

server = Flask(__name__)
server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)

migrate = Migrate(server, db)
manager = Manager(server)
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()