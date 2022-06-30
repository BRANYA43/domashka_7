"""Отримати прогноз погоди для Одеси на наступні 5 днів та записати у файл з ім'ям поточної дати
http://api.openweathermap.org/data/2.5/forecast/daily?q=city&cnt=1&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8
 Параметр cnt = кількість днів
 Параметр q = місто
 Так ми отримаємо та обробимо дату з відповіді (ключ dt):
 datetime.datetime.fromtimestamp(1600419600)
 Застосувавши до отриманого об'єкта дати strftime("%d-%m-%Y") отримаємо строкову дату для запису у файл.
 Приклад імені файлу: 19-09-2020-Odessa-5-days-weather-forecast.txt
 Записаний файл має виглядати так:
 Дата Температура вдень
 18-09-2020 17.86 11.18
 19-09-2020 15.75 11.21
 20-09-2020 20.37 17.49
 21-09-2020 20.75 18.08
 22-09-2020 20.96 17.47
  * Дод. надати користувачеві вибір міста та кількості днів, а також додати колонку Температура вночі"""
import csv
from datetime import datetime

import requests
from requests import Response

from task_2 import get_round_off_number


def create_name_file(city: str, count_days: int) -> str:
    ret = f'{datetime.now().strftime("%d-%m-%Y")} {city.capitalize()} {count_days} days weather forecast.txt'
    return ret.replace(' ', '-')


def set_url(city: str, count_day: int) -> str:
    return f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={count_day}' \
           f'&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8'


def get_response_url_in_json(url: str) -> Response:
    return requests.get(url).json()


def create_dates(response: Response) -> list:
    ret = []
    for date in response['list']:
        ret.append(datetime.fromtimestamp(date['dt']).strftime("%d-%m-%Y"))
    return ret


def create_temperatures(response: Response, key: str) -> list:
    ret = []
    for temp in response['list']:
        ret.append(temp['temp'][key])
    return ret


def create_average_temperatures_two_elem(response: Response, key_1: str, key_2: str) -> list:
    temp_1 = create_temperatures(response, key_1)
    temp_2 = create_temperatures(response, key_2)
    ret = []
    for t1, t2 in zip(temp_1, temp_2):
        ret.append(get_round_off_number((t1 + t2) / 2))
    return ret


def create_temperatures_data(dates: list, t_averages: list, t_days: list, t_nights: list) -> list:
    ret = []
    for date, t_average, t_day, t_night in zip(dates, t_averages, t_days, t_nights):
        ret.append({'date': date, 'temp_average': t_average, 'temp_day': t_day, 'temp_night': t_night})
    return ret


def save_file(name_file: str, data: list):
    with open(name_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=' ')
        writer.writeheader()
        for elem_dict in data:
            writer.writerow(elem_dict)


def main():
    some_city = 'odesa'
    count_d = 5
    some_url = set_url(some_city, count_d)
    some_name_file = create_name_file(some_city, count_d)

    site_response = get_response_url_in_json(some_url)

    dates_list = create_dates(site_response)

    temp_average = create_average_temperatures_two_elem(site_response, 'min', 'max')
    temp_days = create_temperatures(site_response, 'day')
    temp_night = create_temperatures(site_response, 'night')
    temperatures_data = create_temperatures_data(dates_list, temp_average, temp_days, temp_night)

    save_file(some_name_file, temperatures_data)


if __name__ == '__main__':
    main()
