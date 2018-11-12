from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apps.project_register import Project_Home_Page

app = Flask(__name__, static_url_path="/static")
app.config["testing"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:linkinpark09@localhost/NominaRPFDatabase"
app.config.update(dict(SECRET_KEY="09C3BB33B639AD6BFF43D66F56E6E47D18D10FB75285442280D634E9D5DCC4C7",
                       WTF_CSRF_SECRET_KEY="9AAFC9582109C8AF708E9CCC04ECD8A81EA0DDA819D82F5ADA71D78E976B49DD"))


db = SQLAlchemy(app)
app.register_blueprint(Project_Home_Page)

