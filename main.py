# Дарья Трифонова, 25-я когорта — Финальный проект. Инженер по тестированию плюс
from api import new_order, get_order

def test_get_order():
    order_response = new_order({
        "firstName": "Иван",
        "lastName": "Иванюшин",
        "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
        "metroStation": 204,
        "phone": "+34916123451",
        "rentTime": 5,
        "deliveryDate": "2024-12-24",
        "comment": "Самый длинный комментарий, который только можно представить",
        "color": [
            "BLACK"
        ]
    })
    track = order_response.json()["track"]
    get_response = get_order(track)
    assert get_response.status_code == 200