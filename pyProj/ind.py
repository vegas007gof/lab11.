#!/usr/bin/env python3
# -*- coding: utf-8 -*-

schedule = []


def data_input():
    while True:
        global schedule
        schedule.append({
            'название пункта назначения рейса': input('Пункт назначения? - '),
            'номер рейса': int(input('Номер рейса? - ')),
            'тип самолета': input('Тип самолета? - ')
        })
        if input('Напишите "д" чтобы продолжить ввод данных, "н" для завершения ввода.\n') == 'д':
            pass
        else:
            break
    schedule = sorted(schedule, key=lambda row: row['номер рейса'])
    for i in schedule:
        print(i)


def data_search():
    destination = input('Рейс в какой город вас интересует?\n')
    approved = []
    for i in schedule:
        if i['название пункта назначения рейса'] == destination:
            approved.append(i)
    for i in approved:
        print(i)
    if not approved:
        print("По вашему запросу ничего не найдено.\n")


if __name__ == "__main__":
    x = int()
    while True:
        print("1 - Ввести данные\n"
              "2 - Поиск\n"
              "3 - Выход")
        x = int(input())
        if x == 1:
            data_input()
        elif x == 2:
            data_search()
        elif x == 3:
            break
