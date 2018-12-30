from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def get_credentials_urls(connect_api={"user": "", "password": "", "dbname": "", "port": ""}):
    file_lines = open("app/database_config", "rt").readlines()
    for line in file_lines:
        for key, value in connect_api.items():
            if line.split("=")[0] in key and value == "":
                connect_api[key] = line.split("=")[1].replace("\n", "")
    return connect_api

DATABASE_API = get_credentials_urls()

APP = Flask(__name__, static_url_path="/static")
APP.config["SECRET_KEY"] = "09C3BB33B639A"
APP.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://%s:%s@localhost:%s/%s" % (DATABASE_API["user"], DATABASE_API["password"], DATABASE_API["port"], DATABASE_API["dbname"])
DB = SQLAlchemy(APP)

from . import routes