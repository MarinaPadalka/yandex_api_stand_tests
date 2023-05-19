import configuration
import requests
import data

def post_new_user(user_body): # запрос на создание нового пользователя
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, # подставляем полный url
                         json=user_body, # тут тело
                         headers=data.headers) # а здесь заголовки

def post_new_client_kit(kit_body,authToken): # запрос на создание нового набора
    head = data.headers.copy()
    head["Authorization"] = "Bearer" + authToken
    return requests.post(configuration.URL_SERVICE + configuration.NEW_CLIENT_KIT,
                         json=kit_body,
                         headers=head)
