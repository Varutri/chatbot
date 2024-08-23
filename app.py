from flask import Flask, request
import requests


app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']
    print(source_currency)
    print(amount)
    print(target_currency)
    cf = fetch_conversion_factor(source_currency, target_currency,amount)

    print(cf)
    response = {
        'fulfillmentText': "{} {} is {} {}".format(amount, source_currency, cf, target_currency)
    }
    from flask import jsonify
    return jsonify(response)
    return "hello"
#def fetch_conversion_factor(source,target):
    #url = https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_1wI0LEMx8tOKSEOmyDrC4jsDJxCLTH6nx1xk09lm&currencies={}&base_currency={}
    #response = requests.get(url)
    #response = response.json


def fetch_conversion_factor(source, target, amount):
    # Construct the API URL
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_1wI0LEMx8tOKSEOmyDrC4jsDJxCLTH6nx1xk09lm&currencies={target}&base_currency={source}"

    # Make the GET request
    response = requests.get(url)

    # Parse the JSON response
    data = response.json()

    # Extract the conversion rate for the target currency
    conversion_rate = data['data'][target]

    # Calculate the converted amount
    converted_amount = conversion_rate * amount
    return converted_amount


if __name__=="__main__" :
    app.run(debug=True)



