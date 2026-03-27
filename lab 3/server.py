from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    param = request.args.get('param', type=int)
    if param is None:
        return jsonify({'error': 'param required'}), 400
    
    number = random.randint(1, 100)
    result = number * param
    operation = random.choice(['sum', 'sub', 'mul', 'div'])
    
    return jsonify({
        'result': result,
        'operation': operation
    })


@app.route('/number/', methods=['POST'])
def post_number():
    data = request.get_json()
    if data is None or 'jsonParam' not in data:
        return jsonify({'error': 'jsonParam required'}), 400
    
    param = data['jsonParam']
    number = random.randint(1, 100)
    result = number * param
    operation = random.choice(['sum', 'sub', 'mul', 'div'])
    
    return jsonify({
        'result': result,
        'operation': operation
    })


@app.route('/number/', methods=['DELETE'])
def delete_number():
    number = random.randint(1, 100)
    operation = random.choice(['sum', 'sub', 'mul', 'div'])
    
    return jsonify({
        'result': number,
        'operation': operation
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)