from app import DB

project = DB.Table('project_info',
    DB.Column('project_id', DB.Integer, DB.ForeignKey('projects.id'), primary_key=True),
    DB.Column('employee_id', DB.Integer, DB.ForeignKey('employee.id'), primary_key=True)
)

class Project(DB.Model):
    __tablename__ = "projects"
    id = DB.Column(DB.Integer, primary_key=True)
    name_project = DB.Column(DB.String(100), nullable=False)
    project_owner = DB.Column(DB.String(100), nullable=False)
    all_project_info = DB.relationship('Employee', secondary=project, lazy='subquery', backref=DB.backref('projects_work', lazy=True))

    def __repr__(self):
        return "Name of project: %r, Name of project owner %r" % (self.name_project, self.project_owner)


class Employee(DB.Model):
    __tablename__ = "employee"
    id = DB.Column(DB.Integer, primary_key=True)
    employee_name = DB.Column(DB.String(100), nullable=False)
    work_type_employee = DB.Column(DB.String(100), nullable=False)
    days_worked = DB.Column(DB.String(100), nullable=False)
    extra_hours = DB.Column(DB.Integer(), nullable=False)
    pay_for_hours = DB.Column(DB.Integer(), nullable=False)

    def __repr__(self):
        return "Employee Name: %r, Type Work: %r, Extra Hours: %r, Pay Hours: %r" % (self.employee_name, self.work_type_employee, self.extra_hours, self.pay_for_hours)

DB.create_all()