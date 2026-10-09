from multiprocessing.managers import Token

import requests


#1 Зарегистрировать пользователя и отправить токен на почту

session = requests.Session()

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Liza', 'last_name': 'Viaznikova','email': "eliza.vyaznikova@yandex.ru", "password": "Study2026@",
#           'company': 'Ситилинк', 'position': 'Менеджер', 'type' : 'shop'
#           },
# )
#
# print(response.json())


# 2 Подтверждение e-mail токеном из письма
#
# response = session.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#         json = {"email": "eliza.vyaznikova@yandex.ru", "token" : 'cb0b3eb4dde50795c9950399c0b9daa2f60f435d' })
# print(response.status_code)
# print(response.json())

# 3 Теперь авторизуемся и получаем данные по Токену.

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "eliza.vyaznikova@yandex.ru", "password": "Study2026@"},
# )
# print(response.status_code)
# print(response.json())
# token = response.json()['Token']
# print(token)
#
# headers = {
#     "Authorization": f"Token {token}",
#     "Accept": "application/json"
# }
#
# response2 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response2.status_code)
# print(response2.json())

# 4 Теперь авторизуемся и правим данные данные по Токену.

response = session.post(
    "http://127.0.0.1:8000/api/v1/user/login",
    json={'email': "eliza.vyaznikova@yandex.ru", "password": "Diplom2026@"},
)
print(response.status_code)
print(response.json())
token = response.json()['Token']
print(token)

headers = {
    "Authorization": f"Token {token}",
    "Accept": "application/json"
}

response2 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)

print(response2.status_code)
print(response2.json())

response3 = session.post('http://127.0.0.1:8000/api/v1/user/details', headers= headers,
        json={'company': 'Ситилинк', "password": 'Study2026@', 'position': 'Менеджер'},
                         )

response4 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)

print(response4.status_code)
print(response4.json())


