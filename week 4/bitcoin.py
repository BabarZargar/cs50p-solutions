import requests
import sys


if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)



try:
    n = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

API_KEY = "99c76148c6d3da6561f7114c16b9e6201fe74b60d32ed49b75002ccfbb588fec"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin", headers=headers)

except requests.RequestException:
     print("Server issue")
     sys.exit(1)

else:

    data = response.json()

    price = float(data["data"]["priceUsd"])
 
    total = n * price

    print(f"${total:,.4f}")





