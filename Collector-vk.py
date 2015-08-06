# -*- coding: utf-8 -*-
"""
Документация к модулю
"""
__author__ = 'Termvsrobo'

#import sqlite3
import vk_api

import settings

#Авторизация
login, password = settings.login, settings.password
vk = vk_api.VkApi(login, password)
try:
    vk.authorization()
    authorized = True
except:
    authorized = False
    print 'Not authorized'

#Подключаемся к базе данных SQLite3
#conn = sqlite3.connect(settings.db)
#database = conn.cursor()


#Из строки выбираем только цифры. Функция возвращает номер телефона друга
def process_number(number):
    """
    Документация к функции
    """
    num_string = ''
    if number.isdigit():
        return number
    else:
        for k in number:
            if k.isdigit():
                num_string += k
        return num_string

#Список номеров
list_numbers = []

if authorized:
    #Получаем список друзей
    friends = vk.method('friends.get', {'user_ids': None})['items']
    for friend in friends:
        try:
            #Получаем информацию о человеке
            user_info = vk.method('users.get', {'user_ids': friend,
                                                'fields': 'sex, bdate, city, \
                                                country, online_mobile, \
                                                domain, has_mobile, contacts, \
                                                connections, site, education, \
                                                universities, schools, \
                                                common_count, relation, \
                                                relatives, counters, \
                                                screen_name, maiden_name, \
                                                timezone, occupation, \
                                                activities, interests, music, \
                                                movies, tv, books, games, \
                                                about, quotes, personal'})
            domain = user_info[0]['domain']
            last_name = user_info[0]['last_name']
            university_name = user_info[0]['university_name']
            site = user_info[0]['site']
            sex = user_info[0]['sex']
            quotes = user_info[0]['quotes']
            user_ids = user_info[0]['id']
            bdate = user_info[0]['bdate']
            city = user_info[0]['city']
            country = user_info[0]['country']
            #online_mobile = user_info[0]['online_mobile']
            has_mobile = user_info[0]['has_mobile']
            #contacts = user_info[0]['contacts']
            #connections = user_info[0]['connections']
            #education = user_info[0]['education']
            universities = user_info[0]['universities']
            schools = user_info[0]['schools']
            common_count = user_info[0]['common_count']
            relation = user_info[0]['relation']
            relatives = user_info[0]['relatives']
            counters = user_info[0]['counters']
            screen_name = user_info[0]['screen_name']
            #maiden_name = user_info[0]['maiden_name']
            #timezone = user_info[0]['timezone']
            occupation = user_info[0]['occupation']
            activities = user_info[0]['activities']
            interests = user_info[0]['interests']
            music = user_info[0]['music']
            movies = user_info[0]['movies']
            tv = user_info[0]['tv']
            books = user_info[0]['books']
            games = user_info[0]['games']
            about = user_info[0]['about']
            personal = user_info[0]['personal']
            #Получаем список сообществ человека
            groups = vk.method('groups.get', {'user_ids': friend,
                                              'fields': 'city, country, place,\
                                              description, wiki_page, \
                                              members_count, counters, \
                                              start_date, finish_date, \
                                              activity, status, contacts, \
                                              links, fixed_post, verified, \
                                              site'})

            for group in groups:
                group_info = vk.method('groups.getById', {'group_id': group,
                                                          'fields': 'city, \
                                                          country, place, \
                                                          description, \
                                                          wiki_page, \
                                                          members_count, \
                                                          counters, \
                                                          start_date, \
                                                          finish_date, \
                                                          activity, status, \
                                                          contacts, links, \
                                                          fixed_post, \
                                                          verified, site'})

            mobile = process_number(user_info[0]['mobile_phone'])
            if len(mobile) > 0:
                list_numbers.append(mobile)
        except:
            continue

    print list_numbers
