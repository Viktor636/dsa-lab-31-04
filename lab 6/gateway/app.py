from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Адреса микросервисов
CURRENCY_MANAGER = 'http://localhost:5001'
DATA_MANAGER = 'http://localhost:5002'


@app.route('/')
def index():
    # Получаем результат из URL 
    message = request.args.get('message')
    error = request.args.get('error')
    convert_result = request.args.get('convert_result')
    
    return render_template('index.html', 
                         message=message, 
                         error=error, 
                         convert_result=convert_result)

@app.route('/currencies_page')
def currencies_page():
    resp = requests.get(f'{DATA_MANAGER}/currencies')
    currencies = resp.json()
    return render_template('currencies.html', currencies=currencies)


# Добавление валюты
@app.route('/add', methods=['POST'])
def add_currency():
    name = request.form.get('currency_name')
    rate = request.form.get('rate')
    
    resp = requests.post(f'{CURRENCY_MANAGER}/load', 
                        json={'currency_name': name, 'rate': float(rate)})
    result = resp.json()
    
    if 'error' in result:
        return redirect(url_for('index', error=result['error']))
    else:
        return redirect(url_for('index', message=result['message']))


# Обновление курса
@app.route('/update', methods=['POST'])
def update_currency():
    name = request.form.get('currency_name')
    rate = request.form.get('rate')
    
    resp = requests.post(f'{CURRENCY_MANAGER}/update_currency', 
                        json={'currency_name': name, 'rate': float(rate)})
    result = resp.json()
    
    if 'error' in result:
        return redirect(url_for('index', error=result['error']))
    else:
        return redirect(url_for('index', message=result['message']))


# Удаление валюты
@app.route('/delete', methods=['POST'])
def delete_currency():
    name = request.form.get('currency_name')
    
    resp = requests.post(f'{CURRENCY_MANAGER}/delete', 
                        json={'currency_name': name})
    result = resp.json()
    
    if 'error' in result:
        return redirect(url_for('index', error=result['error']))
    else:
        return redirect(url_for('index', message=result['message']))


# Конвертация
@app.route('/convert', methods=['POST'])
def convert_currency():
    currency = request.form.get('currency')
    amount = request.form.get('amount')
    
    resp = requests.get(f'{DATA_MANAGER}/convert', 
                       params={'currency': currency, 'amount': amount})
    result = resp.json()
    
    if 'error' in result:
        return redirect(url_for('index', error=result['error']))
    else:
        # Cообщение для конвертации
        msg = f"{amount} {currency} = {result['result_rub']} руб. (курс: {result['rate']})"
        return redirect(url_for('index', message=msg))

if __name__ == '__main__':
    app.run(port=5000, debug=True)