# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая”
# и т.п. Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст
# не соответсвует формату.

# Дорабатываем задачу 4. Добавьте возможность запуска из командной строки. При
# этом значение любого параметра можно опустить. В этом случае берётся первый
# в месяце день недели, текущий день недели и/или текущий месяц.

import argparse
import datetime
from task02 import log_decor

MONTHS ={'января':1,'февраля':2,'марта':3,'апреля':4,'мая':5,'июня':6,
         'июля':7,'августа':8,'сентября':9,'октября':10,'ноября':11,'декабря':12}
MONTHSREVERSED = dict(map(lambda x: (x[1], x[0]), MONTHS.items()))

WEEKDAYS={'понедельник':1,'вторник':2,'среда':3,'четверг':4,
          'пятница':5,'суббота':6,'воскресенье':7}
WEEKDAYSREVERSED = dict(map(lambda x: (x[1], x[0]), WEEKDAYS.items()))

@log_decor
def print_date(str_date: str):
    num_day, weekday, month = str_date.split()
    num_day = int(num_day[0])
    weekday = WEEKDAYS[weekday]-1
    month = MONTHS[month]
    week_counter = 1
    for i in range(1, 32):
        work_date = datetime.datetime(year = datetime.datetime.now().year, month = month, day = i)
        if work_date.weekday() == weekday:
            if week_counter == num_day:
                return work_date
            week_counter += 1
    raise ValueError

def parser():
    parser = argparse.ArgumentParser(description='print_date parser')
    parser.add_argument('-n','--numday', default = 1)
    parser.add_argument('-w', '--weekday', default=WEEKDAYSREVERSED.get(
        datetime.datetime.now().weekday(), 'понедельник'))
    parser.add_argument('-m','--month', default = MONTHSREVERSED.get(datetime.datetime.now().month, 'января'))
    args = parser.parse_args()
    return print_date(f'{args.numday}-ый {args.weekday} {args.month}')

if __name__ == '__main__':
    # print(print_date('3-й воскресенье октября'))
    # python Seminar15/home01.py -n 1 -w воскресенье -m октября
    print(parser())