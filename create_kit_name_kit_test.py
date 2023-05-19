import configuration
import requests
import sender_stand_request
import data

def get_token(): # запрос на получение токена
    user_body = data.user_body
    return sender_stand_request.post_new_user(user_body).json()["authToken"]

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    kit_body = get_kit_body(name)
    authToken = get_token()
    new_client_kit_response = sender_stand_request.post_new_client_kit(kit_body,authToken)

    assert new_client_kit_response.status_code == 201
    assert new_client_kit_response.json()["name"] == name

# Функция для негативной проверки
def negative_assert(name):
    kit_body = get_kit_body(name)
    authToken = get_token()
    new_client_kit_response = sender_stand_request.post_new_client_kit(kit_body,authToken)

    assert new_client_kit_response.status_code == 400


#Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_user_kit_has_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_user_kit_has_511_letters_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Ошибка. Параметр name состоит из 0 символов
def test_create_user_kit_has_0_letters_in_name_get_error_response():
    negative_assert("")

# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_user_kit_has_512_letters_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabca")

# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_user_kit_has_english_letters_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_user_kit_has_russian_letters_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Успешное создание набора. Параметр name состоит из спецсимволов
def test_create_user_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")

# Тест 8. Успешное создание набора. Параметр name содержит пробелы
def test_create_user_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")

# Тест 9. Успешное создание набора. Параметр name содержит цифры
def test_create_user_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Тест 10. Ошибка. Параметр name не передан в запросе
def test_create_user_kit_no_first_name_get_error_response(auth=get_token()):
    head = data.headers.copy()
    head["Authorization"] = auth
    kit_body = {}
    user_response = requests.post(configuration.URL_SERVICE + configuration.NEW_CLIENT_KIT,
                                  json=kit_body,
                                  headers=head)
    assert user_response.status_code == 400

# Тест 11. Ошибка. Передан другой тип параметра - число
def test_create_user_kit_name_has_int_get_error_response():
    negative_assert(123)