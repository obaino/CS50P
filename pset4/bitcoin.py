# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import requests
import sys

def main():
    coins = get_coins()
    amount = get_value(coins)
    print(f"${amount:,.4f}")

def get_value(c):
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        o = response.json()
        value = o["bpi"]["USD"]["rate_float"]
        return c * value
    except requests.RequestException:
        sys.exit("There was an ambiguous exception that occurred while handling your request.")

def get_coins():
    try:
        return float(sys.argv[1])
    except (ValueError):
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

if __name__ == "__main__":
    main()