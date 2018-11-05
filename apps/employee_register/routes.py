from flask import Flask, render_template
app = Flask(__name__)

@app.route("/employee_register")
def show_register_employee():
    return render_template('employee_template.html')