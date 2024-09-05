import configuration
import requests
import data
from data import product_ids


def post_products_kits(body):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # inserta la dirección URL completa
                         json=product_ids,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json())