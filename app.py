from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Employee Management Portal"

@app.route('/employees')
def employees():
    return jsonify({
        "message": "Employee list"
    })

if __name__ == '__main__':
    app.run(debug=True)