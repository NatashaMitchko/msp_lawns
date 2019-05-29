from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Lawn name mapped to days open
lawns = [
    {'name': 'veterans',
     'days_open': [2, 3, 5, 6]},
    {'name': 'oval',
     'days_open': [2, 3, 5, 6]},
    {'name': 'magnolia',
     'days_open': [0, 1, 4]},
    {'name': 'sol_lewitt',
     'days_open': [0, 1, 4]},
    {'name': 'sparrow',
     'days_open': [0, 1, 4]},
    {'name': 'cherry',
     'days_open': [2, 3, 5, 6]},
    {'name': 'farragut',
     'days_open': [2, 3, 5, 6]},
    {'name': 'redbud',
     'days_open': [0, 1, 4]}
]

@app.route('/')
def index():
    """
    Homepage
    """
    return render_template('index.html')

@app.route('/lawn-status')
def get_lawn_status():
    """
    Return a map of lawns to bool, True if the lawn is open today
    """
    lawn_status = {}
    for lawn in lawns:
        if datetime.today().weekday()  in lawn['days_open']:
            lawn_status[lawn['name']] = True
        else:
            lawn_status[lawn['name']] = False
    return jsonify(lawn_status)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')