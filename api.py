import requests

SERVER_URL = "https://f296bd7c-0c4b-429a-96fe-b5ec5b774b9c.serverhub.praktikum-services.ru"

def new_order(json):
    return requests.post(SERVER_URL + '/api/v1/orders',
                         json=json,
                         headers={}
                         )
def get_order(order_track: int):
    return requests.get(SERVER_URL + '/api/v1/orders/track',
                        params={
                            't': order_track
                        })