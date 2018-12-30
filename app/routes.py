from flask import Flask, render_template, request, redirect, url_for
from app.models import Project, Employee
from app.forms import AddProjectForm, AddEmployeeForm
from app import DB, APP

@APP.route("/homepage")
@APP.route("/")
def home_page():
    projects = Project.query.all()
    return render_template("home_page.htm", projects=projects)

@APP.route("/add_employee", methods=['GET', 'POST'])
def add_employees():
    employee_form = AddEmployeeForm()
    if request.method == "POST":
        days_worked_checked = ",".join(request.form.getlist('days'))
        add_employee_model = Employee(employee_name=employee_form.name_employee.data, work_type_employee=employee_form.work_type_of_employee.data, days_worked=days_worked_checked, extra_hours=employee_form.extra_hours.data, pay_for_hours=employee_form.pay_for_days.data)
        DB.session.add(add_employee_model)
        DB.session.commit()
        return redirect(url_for("home_page"))
    else: 
        return render_template('add_employee.htm', form=employee_form, title="crear")

@APP.route("/edit_employees", methods=['GET', 'POST'])
def edit_employees():
    employee_form = AddEmployeeForm()
    if request.method == "POST":
        pass
    else:
        return render_template('edit_employee.htm', form=employee_form)

@APP.route("/add_project", methods = ['GET', 'POST'])
def adding_project():
    adding_project_form = AddProjectForm()
    if request.method == "POST":
        new_project = Project(name_project=adding_project_form.name_project.data, project_owner=adding_project_form.name_owner.data)
        DB.session.add(new_project)
        DB.session.commit()
        return redirect(url_for('home_page'))
    else: 
        return render_template("project_form_page.htm", form=adding_project_form, title="crear")

@APP.route('/edit_project/<int:project_id>', methods = ['GET', 'POST'])
def edit_project(project_id):
    adding_project_form = AddProjectForm()
    project_selected = Project.query.filter_by(id = project_id).first()
    if request.method == "POST":
        project_selected.name_project = adding_project_form.name_project.data
        project_selected.project_owner = adding_project_form.name_owner.data
        DB.session.commit()
        return redirect(url_for("home_page"))
    else:
        return render_template("project_form_page.htm", form=adding_project_form, title="editar", projectName=project_selected.name_project, ownerName=project_selected.project_owner)