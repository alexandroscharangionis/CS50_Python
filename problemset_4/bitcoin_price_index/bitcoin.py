import requests
import sys

def main():
  get_bitcoin_price()

def get_bitcoin_price():
  btc_rate = get_bitcoin_rate()
  btc_price = btc_rate * float(sys.argv[1])
  print(f'${btc_price:,.4f}')

def get_bitcoin_rate():
  try:
    if float(sys.argv[1]):
      req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      json_req = req.json()
      for item in json_req['bpi']['USD']:
        if item == 'rate_float':
          return json_req['bpi']['USD']['rate_float']
  except ValueError:
    sys.exit('Command line argument is not a number')
  except IndexError:
    sys.exit('Missing command line argument')
  except requests.RequestException:
    sys.exit('Something went wrong with your request.')

main()