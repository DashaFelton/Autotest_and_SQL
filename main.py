# Дарья Трифонова, 25-я когорта — Финальный проект. Инженер по тестированию плюс
import data
from api import new_order, get_order

def test_get_order():
    order_response = new_order(data.order_new)
    track = order_response.json()["track"]
    get_response = get_order(track)
    assert get_response.status_code == 200