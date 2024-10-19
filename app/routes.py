from flask import Blueprint, jsonify, request
from app.calculator import add, subtract, multiply, divide

bp = Blueprint('calculator', __name__)

@bp.route('/<operation>/<num1>/<num2>', methods=['GET', 'POST'])
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
        num1 = float(num1)
        num2 = float(num2)
        
        result = operations[operation](num1, num2)
        print(f"Result: {result}")
        return jsonify({'status': 200, 'result': result})
    except ValueError:
        print("Invalid number format")
        return jsonify({'status': 400, 'error': 'Invalid number format'}), 400
    except ZeroDivisionError:
        print("Division by zero")
        return jsonify({'status': 400, 'error': 'Division by zero'}), 400
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 500, 'error': str(e)}), 500