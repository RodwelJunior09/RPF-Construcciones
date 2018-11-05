from flask import Flask, render_template, request
from .project_register_form import RegisterForm
from . import Project_Home_Page

app = Flask(__name__)
app.secret_key = ""

@Project_Home_Page.route("/")
def return_home_page():
    return render_template("home_page.htm")

@Project_Home_Page.route("/addingProject", methods = ["GET", "POST"])
def returnAddingProject():
    register_form = RegisterForm()
    if request.method == "POST":
        return render_template("adding_project.htm", form = register_form)
    else:
        return render_template("adding_project.htm", form = register_form)