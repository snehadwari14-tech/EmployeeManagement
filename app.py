from flask import Flask, request, jsonify

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return "Employee Management Portal"

# Display all employees
@app.route('/employees')
def employees_list():
    return jsonify(employees)

# Employee Registration
@app.route('/register', methods=['POST'])
def register_employee():

    data = request.json

    employee = {
        "id": len(employees) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }

    employees.append(employee)

    return jsonify({
        "message": "Employee Registered Successfully",
        "employee": employee
    })

# Employee Search
@app.route('/search/<name>')
def search_employee(name):

    result = []

    for employee in employees:
        if name.lower() in employee["name"].lower():
            result.append(employee)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)