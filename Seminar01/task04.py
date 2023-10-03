"""
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетради
"""
TWO = 2
TEN = 10
COLUMNS = 5

for i in range(TWO,TEN,COLUMNS):
    for j in range(TWO,TEN+1):
        for k in range(i, i+COLUMNS):
            #print('{} * {} = {}'.format(k, j, k*j), end='\t')
            print(f'{k:>3} *{j:>3} ={k * j :>3}', end='\t')
        print()
    print()
