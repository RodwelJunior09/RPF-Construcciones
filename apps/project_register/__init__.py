from flask import Blueprint, render_template, abort, Request
from .project_register_form import RegisterForm

Project_Home_Page = Blueprint('projects_view', __name__, template_folder='templates')

from . import routes