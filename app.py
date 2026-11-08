from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Rahul", "email": "rahul@gmail.com"},
    {"id": 2, "name": "Priya", "email": "priya@gmail.com"},
    {"id": 3, "name": "Amit", "email": "amit@gmail.com"}
]

@app.route('/')
def home():
    return "Employee Management Portal"

@app.route('/search/<name>')
def search_employee(name):

    result = []

    for employee in employees:
        if name.lower() in employee["name"].lower():
            result.append(employee)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)