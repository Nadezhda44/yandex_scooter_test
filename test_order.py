# Надежда Калина, 43-я когорта — Финальный проект. Инженер по тестированию плюс

import stand_request

def test_get_order_by_track_success():
    # Шаг 1: Выполнить запрос на создание заказа через функцию
    response_create = stand_request.post_new_order()
    
    # Шаг 2: Получаем и сохраняем номер трека заказа
    track_number = response_create.json()["track"]
    
    # Шаг 3: Выполняем запрос на получение заказа по треку
    response_get = stand_request.get_order_by_track(track_number)
    
    # Шаг 4: Проверяем условие (информация о заказе успешно получена) - код 200
    assert response_get.status_code == 200