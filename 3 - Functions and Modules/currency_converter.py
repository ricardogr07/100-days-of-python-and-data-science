import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount
    else:
        return "Error: Unable to fetch conversion rate."