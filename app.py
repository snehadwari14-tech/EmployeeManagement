from flask import Flask, request, jsonify

app = Flask(__name__)

employees = []

@app.route('/')
def home():
    return "Employee Management Portal"

@app.route('/employees')
def employees_list():
    return jsonify({
        "message": "Employee list"
    })

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

if __name__ == '__main__':
    app.run(debug=True)