from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔑ExchangeRate-API key
API_KEY = "ac03febdd0c4fcc25dd3792f"

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    # 🔹 Dialogflow parameters (correct structure)
    source_currency = data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount = data['queryResult']['parameters']['unit-currency'][0]['amount']
    target_currency = data['queryResult']['parameters']['currency-name'][0]

    # 🔹 Fetch conversion rate
    rate = fetch_conversion_factor(source_currency, target_currency)

    final_amount = round(amount * rate, 2)

    # 🔹 Dialogflow response
    response = {
        "fulfillmentText": f"{amount} {source_currency} is {final_amount} {target_currency}"
    }

    return jsonify(response)


def fetch_conversion_factor(source, target):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{source}"
    response = requests.get(url).json()
    return response['conversion_rates'][target]


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

