import os

class Config:
    API_URL = os.environ.get('API_URL', 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    FLASK_APP = os.environ.get('FLASK_APP', 'api/app.py')
    FLASK_RUN_HOST = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    FLASK_RUN_PORT = int(os.environ.get('FLASK_RUN_PORT', '5000'))
