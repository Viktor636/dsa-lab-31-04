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

# Создаём таблицу
with app.app_context():
    db.create_all()

# Эндпоинт для добавления валюты
@app.route('/load', methods=['POST'])
def load():
    data = request.get_json()
    
    if not data or not data.get('currency_name') or not data.get('rate'):
        return jsonify({'error': 'Заполните данные'}), 400
    
    exists = Currency.query.filter_by(currency_name=data['currency_name']).first()
    if exists:
        return jsonify({'error': 'Такая валюта уже есть'}), 400
    
    new_curr = Currency(currency_name=data['currency_name'], rate=data['rate'])
    db.session.add(new_curr)
    db.session.commit()
    
    return jsonify({'message': 'Валюта добавлена'}), 200

# Эндпоинт для обновления курса
@app.route('/update_currency', methods=['POST'])
def update():
    data = request.get_json()
    
    curr = Currency.query.filter_by(currency_name=data.get('currency_name')).first()
    if not curr:
        return jsonify({'error': 'Валюта не найдена'}), 404
    
    curr.rate = data.get('rate')
    db.session.commit()
    
    return jsonify({'message': 'Курс обновлён'}), 200

# Эндпоинт для удаления валюты
@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    
    curr = Currency.query.filter_by(currency_name=data.get('currency_name')).first()
    if not curr:
        return jsonify({'error': 'Валюта не найдена'}), 404
    
    db.session.delete(curr)
    db.session.commit()
    
    return jsonify({'message': 'Валюта удалена'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)