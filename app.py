from flask import Flask
import finnhub

finnhub_client = finnhub.Client(api_key="c2fdbl2ad3ien4444lpg")

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/percent-change/<ticker>")
def percent_change(ticker):
	quote = finnhub_client.quote(ticker)
	return ((quote['c'] - quote['o']) / quote['o']) * 100

@app.route("/get-range/<ticker>/<sensitivity>")
def get_sensitivity_range(ticker, sensitivity):
	pass