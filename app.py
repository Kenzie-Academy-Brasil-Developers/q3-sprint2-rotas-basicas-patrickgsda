from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    my_dict = {'data': 'Hello Flask'}
    return my_dict

@app.route('/current_datetime', methods=['GET'])
def current_datetime():
    date = datetime.now()
    hour = int(date.strftime('%H'))
    if hour < 12:
        message = 'Bom dia!'
    elif hour >= 12 and hour <= 18:
        message = 'Boa tarde!'
    else:
        message = 'Boa noite!'
        
    dict_return = {'current_datetime': date, 'message': message}
    return dict_return