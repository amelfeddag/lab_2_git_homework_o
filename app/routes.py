from flask import Blueprint, jsonify, request
from app.calculator import add, subtract, multiply, divide

bp = Blueprint('calculator', __name__)

@bp.route('/<operation>/<float:num1>/<float:num2>', methods=['GET', 'POST'])
def calculate(operation, num1, num2):
    print(f"Received operation: {operation}, num1: {num1}, num2: {num2}")
    
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    if operation not in operations:
        print("Invalid operation")
        return jsonify({'status': 400, 'error': 'Invalid operation'}), 400
    
    try:
        result = operations[operation](num1, num2)
        print(f"Result: {result}")
        return jsonify({'status': 200, 'result': result})
    except ZeroDivisionError:
        print("Division by zero")
        return jsonify({'status': 400, 'error': 'Division by zero'}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 500, 'error': str(e)}), 500

# project/main.py
from app import create_app

app = create_app()

@app.route('/')
def index():
    return "Welcome to the Calculator API!"

if __name__ == "__main__":
    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)