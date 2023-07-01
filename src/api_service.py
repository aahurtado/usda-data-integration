import requests

url = 'http://localhost:8080/'
headers = {'Content-Type': 'application/json'}

def create_product(product):
    response = requests.post(url + 'products', json=product, headers=headers)
    if response.status_code == 201:
        return True
    else:
        return False
