#Павел М. 9-когорта, финальный проект. Инженер по тестированию плюс.

import sender_stand_request


def test_positive_status_code_200():
    user_responce = sender_stand_request.get_order_by_track()
    assert user_responce.status_code == 200