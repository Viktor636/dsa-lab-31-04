from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/currencies_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Currency(db.Model):
    __tablename__ = 'currencies'
    id = db.Column(db.Integer, primary_key=True)
    currency_name = db.Column(db.String(50), unique=True, nullable=False)
    rate = db.Column(db.Numeric(10, 4), nullable=False)

# Конвертация валюты
@app.route('/convert', methods=['GET'])
def convert():
    curr_name = request.args.get('currency')
    amount = request.args.get('amount', type=float)
    
    if not curr_name or amount is None:
        return jsonify({'error': 'Укажите currency и amount'}), 400
    
    curr = Currency.query.filter_by(currency_name=curr_name).first()
    if not curr:
        return jsonify({'error': 'Валюта не найдена'}), 404
    
    result = amount * float(curr.rate)
    
    return jsonify({
        'amount': amount,
        'currency': curr_name,
        'rate': float(curr.rate),
        'result_rub': round(result, 2)
    }), 200

# Список всех валют
@app.route('/currencies', methods=['GET'])
def currencies():
    all_curr = Currency.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.currency_name,
        'rate': float(c.rate)
    } for c in all_curr])

if __name__ == '__main__':
    app.run(port=5002, debug=True)