from multiprocessing.managers import Token
from pathlib import Path
import requests
import json
import os
from pprint import pprint
from dotenv import load_dotenv

# Авторизоваться и получить токен

# response = requests.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': "svz84@yandex.ru", "password": "Study2026@"},
# )
# print(response.status_code)
# print(response.json())
# dict1 = response.json()
# token = dict1['Token']
# print(token)

# Зарегистрировать пользователя

# response = requests.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Julia', 'last_name': 'Viaznikova','email': "aum2005@rambler.ru", "password": "Study2026@",
#           'company': 'sitilink', 'position': 'manager', 'type': 'shop'
#           },
# )
#
# print(response.json())


# 1 Зарегистрировать пользователя и отправить токен на почту
#
session = requests.Session()
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
#         json = {"email": "cryptoingsvz@gmail.com", "token" : 'e7c2cf5e75fff16717b21d518905033ce72' })
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

#4 Теперь авторизуемся и правим данные данные по Токену.

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
#         json={'company': 'Ситилинк', "password": "Study2026@", 'position': 'Менеджер'},
#                          )
#
# response4 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response4.status_code)
# print(response4.json())

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
# #base_dir = os.path.abspath(os.path.dirname(__file__))
# #url1 = os.path.join(base_dir, 'data', 'shop1.yaml')
# #url1 ='http://127.0.0.1:8000/path/data/shop1.yaml'
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/products?shop_id=2', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь
#
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

# 11 удаляем контакты

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

# Проверяем статус партнера

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
# response2 = session.get('http://127.0.0.1:8000/api/v1/partner/state', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

# Меняем статус партнера и получаем информацию о новом статусе
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/partner/state', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь
# print(response2.json()['id'])
#
# headers = {
#     "Authorization": f"Token {token}",
#     "Accept": "application/json"
# }
#
# response3 = session.put('http://127.0.0.1:8000/api/v1/partner/state', headers= headers,
#     data={'state': True },   )
#
# print(response3.status_code)
# #pprint(response3.json())  # Получаем словарь
#
# response4 = session.get('http://127.0.0.1:8000/api/v1/partner/state', headers= headers)
#
#
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь


# выводим список товаров и получаем информацию из корзины

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
# response2 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

#13 регистрируем покупателя
# 1 Зарегистрировать пользователя и отправить токен на почту



# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Oleg', 'last_name': 'Ivanov','email': "vspetrowich@gmail.com", "password": "Diplom2026@",
#         'company': 'NGTU', 'position': 'sysadmin',
#           },
# )
#
# print(response.json())


#2 Подтверждение e-mail токеном из письма
#
# response = session.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#         json = {"email": "vspetrowich@gmail.com", "token" : 'af82244fd4e6adb626d' })
# print(response.status_code)
# print(response.json())

#3 Теперь авторизуемся и получаем данные по Токену.

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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

#4 добавлям данные пользователя в базу

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
#         data={'phone': "89234545777", "city": "Бердск", "street": "Ленина", 'house': '14', 'apartment': '12' },
#                          )
# print(response2.status_code)
#
# response3 = session.get('http://127.0.0.1:8000/api/v1/user/contact', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

#14 выводим список товаров доступных для покупки

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# response2 = session.get('http://127.0.0.1:8000/api/v1/products?shop_id=2', headers= headers)
#
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь
#
# response5 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response5.status_code)
# print(response5.json())
#
# print(response5.json()['id'])
#
# print('Печатаем корзину:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# response4 = session.post('http://127.0.0.1:8000/api/v1/basket', headers= headers,
#         data = { "items" : '[ { "product_info": 37,  "quantity": 4 },'
#                            ' {  "product_info": 34, "quantity": 1 }  ]' } )
#
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь
#
# print('Печатаем корзину:')
# response6 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response6.status_code)
# pprint(response6.json())  # Получаем словарь

#Пробуем изменить количество товара

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# print('Печатаем корзину:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
# print("Изменяем количество на 2")
# response7 = session.put('http://127.0.0.1:8000/api/v1/basket', headers= headers,
#         data = { "items" : '[ { "id": 1,  "quantity": 2 }, { "id": 2,  "quantity": 1 }  ]' } )
#
# print(response7.status_code)
# pprint(response7.json())  # Получаем словарь
#
#
# print('Печатаем корзину:')
# response8 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response8.status_code)
# pprint(response8.json())  # Получаем словарь

# Удаляем позицию из корзины
#
# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# print('Печатаем корзину:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
# print("Удаляем позицию из корзины")
# response7 = session.delete('http://127.0.0.1:8000/api/v1/basket', headers= headers,
#         data = { "items" : 2 } )
#
# print(response7.status_code)
# pprint(response7.json())  # Получаем словарь
#
#
# print('Печатаем корзину:')
# response8 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response8.status_code)
# pprint(response8.json())  # Получаем словарь

# Проверяем что всё работает по запросу корзины из БД
#
# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# print('Печатаем корзину:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

# Получаем заказы по партнеру после авторизации

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
# print('Печатаем заказы:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/partner/orders', headers= headers)
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

# Получаем заказы покупателя после авторизации

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# print('Печатаем заказы:')
# response2 = session.get('http://127.0.0.1:8000/api/v1/order', headers= headers)
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

# Пробуем опубликовать заказ из корзины

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
#
#
# response2 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response2.status_code)
# print(response2.json())
# id_cont = response2.json()['contacts'][0]['id']
# print(id_cont)
#
# print('Печатаем заказы:')
# response5 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
# print(response5.status_code)
# pprint(response5.json())  # Получаем словарь
# id_ord = response5.json()[0]['id']
# print(id_ord)
#
# print('Меняем статус заказа:')
# response3 = session.post('http://127.0.0.1:8000/api/v1/order', headers= headers,
#         data = { "id" : id_ord , 'contact' : id_cont }
#                          )
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# print('Печатаем заказ с новым статусом:')
# response4 = session.get('http://127.0.0.1:8000/api/v1/order', headers= headers)
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь

# Заказ с нескольких магазинов
#
# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# response5 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response5.status_code)
# print(response5.json())
#
# print(response5.json()['id'])
#
# print('Печатаем корзину:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# response4 = session.post('http://127.0.0.1:8000/api/v1/basket', headers= headers,
#         data = { "items" : '[ { "product_info": 16,  "quantity": 1 },'
#                             ' { "product_info": 22,  "quantity": 2 } ,'
#                             ' { "product_info": 3,  "quantity": 1 },'
#                             ' { "product_info": 5,  "quantity": 1 },'
#                             ' { "product_info": 10,  "quantity": 1 } ]'
#                  } )
#
#
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь
#
# print('Печатаем корзину:')
# response6 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
#
# print(response6.status_code)
# pprint(response6.json())  # Получаем словарь

#Теперь подтвердим заказ и сменим статус
#
# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
#
#
# response2 = session.get('http://127.0.0.1:8000/api/v1/user/details', headers= headers)
#
# print(response2.status_code)
# print(response2.json())
# id_cont = response2.json()['contacts'][0]['id']
# print(id_cont)
#
# print('Печатаем заказы:')
# response5 = session.get('http://127.0.0.1:8000/api/v1/basket', headers= headers)
# print(response5.status_code)
# pprint(response5.json())  # Получаем словарь
# id_ord = response5.json()[0]['id']
# print(id_ord)
#
# print('Меняем статус заказа:')
# response3 = session.post('http://127.0.0.1:8000/api/v1/order', headers= headers,
#         data = { "id" : id_ord , 'contact' : id_cont }
#                          )
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# print('Печатаем заказ с новым статусом:')
# response4 = session.get('http://127.0.0.1:8000/api/v1/order', headers= headers)
# print(response4.status_code)
# pprint(response4.json())  # Получаем словарь

#Теперь просмотрим заказ магазинами
# # магазин 1
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
# print('Печатаем заказы:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/partner/orders', headers= headers)
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь
#
# # магазин 2
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
# print('Печатаем заказы:')
# response3 = session.get('http://127.0.0.1:8000/api/v1/partner/orders', headers= headers)
# print(response3.status_code)
# pprint(response3.json())  # Получаем словарь

# Получаем заказы покупателя после авторизации со статусом "new"

# load_dotenv()
# user_email3 = os.getenv("EMAIL3")
# user3_pass = os.getenv("PASS3")
#
# response = session.post("http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email3, "password": user3_pass},
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
# print('Печатаем заказы:')
# response2 = session.get('http://127.0.0.1:8000/api/v1/order', headers= headers)
# print(response2.status_code)
# pprint(response2.json())  # Получаем словарь

#14 регистрируем покупателя
# 1 Зарегистрировать пользователя и отправить токен на почту


#
# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/register",
#     json={'first_name': 'Igor', 'last_name': 'Petrov','email': "stepfedormining@gmail.com", "password": "Diplom2026@",
#         'company': 'SIBGUTI', 'position': 'sysadmin',
#           },
# )
#
# print(response.json())


#2 Подтверждение e-mail токеном из письма

# response = session.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#         json = {"email": "stepfedormining@gmail.com", "token" : 'ec762977211d9811eef008' })
# print(response.status_code)
# print(response.json())

#3 Теперь авторизуемся и получаем данные по Токену.

# load_dotenv()
# user_email4 = os.getenv("EMAIL4")
# user4_pass = os.getenv("PASS4")
#
# response = session.post(
#     "http://127.0.0.1:8000/api/v1/user/login",
#     json={'email': user_email4, "password": user4_pass},
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