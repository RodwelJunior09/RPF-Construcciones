from flask_wtf import Form
from wtforms import TextField, IntegerField, DateField, SubmitField
from wtforms import validators, ValidationError

class RegisterForm(Form):
    name_project = TextField("Nombre del projecto", [validators.Required("Por favor introduzca el nombre del projecto")])
    name_owner = TextField("Nombre del dueno", [validators.Required("Por favor introduzca el nombre del dueno")])
    submit = SubmitField("Guardar Informacion")
