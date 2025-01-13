import requests
import configuration

def new_order(json):
    return requests.post(configuration.SERVER_URL + '/api/v1/orders',
                         json=json,
                         headers={}
                         )
def get_order(order_track: int):
    return requests.get(configuration.SERVER_URL + '/api/v1/orders/track',
                        params={
                            't': order_track
                        })