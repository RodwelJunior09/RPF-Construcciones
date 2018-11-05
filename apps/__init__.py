from flask import Flask
from apps.project_register import Project_Home_Page

def creating_app(config_type):
    app = Flask(__name__, static_url_path="/static")
    app.config["testing"] = True 
    app.config.update(dict(SECRET_KEY = "the most powerfull key", WTF_CSRF_SECRET_KEY="another key"))

    app.register_blueprint(Project_Home_Page)

    return app