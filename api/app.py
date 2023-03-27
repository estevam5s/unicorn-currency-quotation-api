from flask import Flask, jsonify
from .main import CurrencyQuotation
# from configuration import Config

# app = Flask(__name__)
# app.config.from_object(Config)

# Restante do código do aplicativo Flask

app = Flask(__name__)

@app.route("/cotacao", methods=["GET"])
def get_cotacao():
    cotacao = CurrencyQuotation.get_cotacao()
    return jsonify(cotacao)

if __name__ == "__main__":
    app.run()
