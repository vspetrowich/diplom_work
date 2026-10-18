from multiprocessing.managers import Token

import requests
import os
from pprint import pprint
from dotenv import load_dotenv


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

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "eliza.vyaznikova@yandex.ru", "password": "Diplom2026@"},
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
#
# response3 = session.post('http://127.0.0.1:8000/api/v1/user/details', headers= headers,
#         json={'company': 'Ситилинк', "password": 'Study2026@', 'position': 'Менеджер'},
#                          )
#
# response4 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response4.status_code)
# print(response4.json())

#5 Теперь авторизуемся, получим информацию о пользователе и попробуем загрузить товар в БД

#response = session.post(
#   "http://127.0.0.1:8000/api/v1/user/login",
#    json={'email': "eliza.vyaznikova@yandex.ru", "password": "Study2026@"},
#)
#print(response.status_code)
#print(response.json())
#token = response.json()['Token']
#print(token)
#
#headers = {
#   "Authorization": f"Token {token}",
#    "Accept": "application/json"
#}
#
#response2 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
#print(response2.status_code)
#print(response2.json())
#
#headers = {
#    "Authorization": f"Token {token}",
#    "Accept": "application/json"
#}
#
#
#response3 = session.post('http://127.0.0.1:8000/api/v1/partner/update', headers= headers,
#                         data={'url' : 'http://127.0.0.1:8000/static/shop1.yaml' },           )
#print(response3.status_code)
#print(response3.json())

#6 Теперь пройдем все этапы заново с новым ползователем и магазином.

# 1 Зарегистрировать пользователя и отправить токен на почту
#

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Nikolay', 'last_name': 'Viaznikov','email': "cryptoingsvz@gmail.com", "password": "Study2026@",
#           'company': 'Ситилинк', 'position': 'Менеджер', 'type' : 'shop'
#           },
# )
#
# print(response.json())


#2 Подтверждение e-mail токеном из письма
#
# response = session.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#         json = {"email": "cryptoingsvz@gmail.com", "token" : 'a08875a0b70b205a1c5f630db08405ed69fd06d1996' })
# print(response.status_code)
# print(response.json())

#3 Теперь авторизуемся и получаем данные по Токену.

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "cryptoingsvz@gmail.com", "password": "Study2026@"},
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


#5 Теперь авторизуемся, получим информацию о пользователе и попробуем загрузить товар в БД

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "cryptoingsvz@gmail.com", "password": "Study2026@"},
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
#
# headers = {
#     "Authorization": f"Token {token}",
#     "Accept": "application/json"
# }
#
#
# response3 = session.post('http://127.0.0.1:8000/api/v1/partner/update', headers= headers,
#                          data={'url' : 'http://127.0.0.1:8000/static/shop2.yaml' },           )
# print(response3.status_code)
# print(response3.json())

#6 Теперь пройдем все этапы заново с новым ползователем и магазином.


#6.1 Зарегистрировать пользователя и отправить токен на почту


# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Liza', 'last_name': 'Viaznikova','email': "eliza.vyaznikova@yandex.ru", "password": "Study2026@",
#           'company': 'Ситилинк', 'position': 'Менеджер', 'type' : 'shop'
#           },
# )
#
# print(response.json())


#6.2 Подтверждение e-mail токеном из письма
#
# response = session.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#         json = {"email": "eliza.vyaznikova@yandex.ru", "token" : 'cb0b3eb4dde50795c9950399c0b9daa2f60f435d' })
# print(response.status_code)
# print(response.json())

#6.3 Теперь авторизуемся и получаем данные по Токену.

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

#6.4 Теперь авторизуемся и правим данные данные по Токену.

# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "eliza.vyaznikova@yandex.ru", "password": "Diplom2026@"},
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
#
# response3 = session.post('http://127.0.0.1:8000/api/v1/user/details', headers= headers,
#         json={'company': 'Ситилинк', "password": 'Study2026@', 'position': 'Менеджер'},
#                          )
#
# response4 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response4.status_code)
# print(response4.json())

#6.5 Теперь авторизуемся, получим информацию о пользователе и попробуем загрузить товар в БД

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
#
# headers = {
#     "Authorization": f"Token {token}",
#     "Accept": "application/json"
# }
#
#
# response3 = session.post('http://127.0.0.1:8000/api/v1/partner/update', headers= headers,
#                          data={'url' : 'http://127.0.0.1:8000/static/shop1.yaml' },           )
# print(response3.status_code)
# print(response3.json())

#7 Запрос на список действующих магазинов

# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/shops', headers= headers)
#
# print(response2.status_code)
# print(response2.json())
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/categories', headers= headers)
#
# print(response3.status_code)
# print(response3.json())

#8 Запрос на список товаров по заданым категориям для активных магазинов
#
# load_dotenv()
# user_email1 = os.getenv("EMAIL1")
# user1_pass = os.getenv("PASS1")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email1, "password": user1_pass},
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/products', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email1, "password": user1_pass},
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

#9 Проверяем контракты пользователя

# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

#10 добавлям данные пользователя в базу

# load_dotenv()
# user_email1 = os.getenv("EMAIL1")
# user1_pass = os.getenv("PASS1")
# #print(user_email1)
# #print(user1_pass)
#
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email1, "password": user1_pass},
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
# response2 = session.post('http://127.0.0.1:8000/api/v1/user/contact', headers= headers,
#         data={'phone': "89131234567", "city": "Новосибирск", "street": "Дачная", 'house': '25', 'apartment': '33' },
#                          )
# print(response2.status_code)
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

#10 редактируем данные пользователя в базе контактов

# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email1, "password": user1_pass},
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
# response4 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь
#
# response2 = session.put('http://127.0.0.1:8000/api/v1/user/contact', headers= headers,
#         data={'id': 1, 'phone': "89139876543", "city": "Новосиб", 'building': '2' },
#                          )
# print(response2.status_code)
# print(response2.json())
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

#10 редактируем данные пользователя 2 в базе контактов

# load_dotenv()
# user_email2 = os.getenv("EMAIL2")
# user2_pass = os.getenv("PASS2")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email2, "password": user2_pass},
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
# response2 = session.post('http://127.0.0.1:8000/api/v1/user/contact', headers= headers,
#         data={'phone': "89239090909", "city": "Омск", "street": "Ленина", 'house': '230', 'building': '3', 'apartment': '105' },
#                          )
# print(response2.status_code)
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# response4 = session.post('http://127.0.0.1:8000/api/v1/user/contact', headers= headers,
#         data={'phone': "89608888888", "city": "Омск", "street": "Кирова", 'house': '111',  'apartment': '34' },
#                          )
# print(response4.status_code)
#
# response5 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response5.status_code)
# pprint(response5.json())  # Получаем словарь

#11 удаляем контакты

# load_dotenv()
# user_email2 = os.getenv("EMAIL2")
# user2_pass = os.getenv("PASS2")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email2, "password": user2_pass},
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
# response5 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response5.status_code)
# print(response5.json())
#
# print(response5.json()['id'])
#
# response2 = session.delete('http://127.0.0.1:8000/api/v1/user/contact', headers= headers,
#         data={'user_id' : response5.json()['id'], 'items' : 4 },
#
#                         )
# #print(response2.data['id'])
# print(response2.status_code)
# print(response2.json())
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

#11 выводим список товаров и получаем информацию из корзины

# load_dotenv()
# user_email1 = os.getenv("EMAIL1")
# user1_pass = os.getenv("PASS1")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email1, "password": user1_pass},
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
