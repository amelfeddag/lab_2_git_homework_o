from flask import Blueprint, jsonify
from app.calculator import add, subtract, multiply, divide

bp = Blueprint('calculator', __name__)

@bp.route('/<operation>/<float:num1>/<float:num2>')
def calculate(operation, num1, num2):
    operations = {
        'add': add.add,
        'subtract': subtract.subtract,
        'multiply': multiply.multiply,
        'divide': divide.divide
    }
    
    if operation not in operations:
        return jsonify({'status': 400, 'error': 'Invalid operation'}), 400
    
    try:
        result = operations[operation](num1, num2)
        return jsonify({'status': 200, 'result': result})
    except ZeroDivisionError:
        return jsonify({'status': 400, 'error': 'Division by zero'}), 400
    except Exception as e:
        return jsonify({'status': 500, 'error': str(e)}), 500