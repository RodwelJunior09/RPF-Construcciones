from flask_wtf import Form
from wtforms import TextField, IntegerField, DateField, SubmitField
from wtforms import validators, ValidationError

class AddProjectForm(Form):
    name_project = TextField("Nombre del projecto", [validators.Required("Por favor introduzca el nombre del projecto")])
    name_owner = TextField("Nombre del dueno", [validators.Required("Por favor introduzca el nombre del dueno")])
    submit = SubmitField("Guardar Informacion")


class AddEmployeeForm(Form):
    name_employee = TextField("Nombre del empleado", [validators.Required("Por favor introduzca el nombre del empleado")])
    work_type_of_employee = TextField("Tipo de trabajo", [validators.required("Por favor introduzca el tipo de trabajo del empleado")])
    extra_hours = IntegerField("Cantidad de horas extras")
    pay_for_days = IntegerField("Pago por dia del empleado", [validators.required("Por favor introduzca el pago por dia del empleado")])
    submit_info = SubmitField("Guardar Informacion")