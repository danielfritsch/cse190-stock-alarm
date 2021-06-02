from flask import Flask
from flask_cors import CORS, cross_origin
import finnhub

finnhub_client = finnhub.Client(api_key="c2fdbl2ad3ien4444lpg")

app = Flask(__name__)
CORS(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/percent_change/<ticker>")
def percent_change(ticker):
	quote = finnhub_client.quote(ticker)
	return { 'percent_change': ((quote['c'] - quote['o']) / quote['o']) * 100}

@app.route("/get_sensitivity_range/<ticker>/<sensitivity>")
def get_sensitivity_range(ticker, sensitivity):
	return { 'range': [-1.5, 1.5] }
