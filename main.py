
from config import API_KEY
import requests

url = f'http://data.fixer.io/api/latest?access_key={API_KEY}'


def request_adapter(uri):
    resp = requests.get(url)
    return resp

def get_exchange_rate(request_adapter_f=request_adapter):
    response = request_adapter_f(url)

    while response.status_code != 200:
        response = request_adapter_f(url)   
    data = response.json()

    if data['success'] == True:
        usd = data['rates']['USD']
        gbp = data['rates']['GBP']

        return gbp / usd * 100
    else:
        return "Error getting the information"

if __name__ == '__main__':
    print(get_exchange_rate())