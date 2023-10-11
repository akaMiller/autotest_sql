import configuration
import data
import requests
#Запрос на создание нового заказа
def post_new_order ():
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDERS_PATH, json=data.order_body)

#Запрос на получение трек-номера заказа
def get_track_id():
    responce = post_new_order()
    track = responce.json()['track']
    return track
#Разово получаем трек-номер
track = get_track_id()
print(track)

def get_order_by_track():
    return requests.get( configuration.URL_SERVICE+configuration.GET_ORDERS_PATH + '?t=' + str(track))

