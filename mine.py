poleno=[['f' , '*' , '*' , '*' , '*' , 'f' , '*' , '*' , '*' ],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', 'f', '*', 'f', '*', 'f', '*'],
      ['*', 'f', '*', '*', 'f', 'f', '*', '*', '*'],
      ['*', '*', 'f', '*', '*', '*', 'f', '*', 'f'],
      ['f', '*', 'f', '*', '*', 'f', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', 'f', '*', '*', 'f', '*', '*', 'f', '*'],
      ['*', '*', '*', 'f', '*', '*', '*', '*', '*']]

pole=[['*' , '*' , '*' , '*' , '*' , '*' , '*' , '*' , '*' ],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
      ['*', '*', '*', '*', '*', '*', '*', '*', '*']]

def vuvod(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end=' ')
        print()

import mine

mine.vuvod(mine.pole)

def check(stroka, stolb):
    pass

game = True
while game:
    stroka = int(input('Строка:'))
    stolb = int(input('Столбик:'))

    mine.check(stroka - 1, stolb - 1)
    mine.vuvod(mine.pole)
print('Всё поле открыто!')

def check(stroka, stolb):
    if pole[stroka][stolb]=='*':
        pole[stroka][stolb] = poleno[stroka][stolb]
        if poleno[stroka][stolb]=='f':
            if stroka-1 >=0:
                check(stroka-1, stolb)
                if stolb-1 >=0:
                   check(stroka-1, stolb-1)

                if stolb+1 < len(poleno[stroka]):
                    check(stroka-1,stolb+1)

            if stroka+1 < len(poleno):
                check(stroka+1, stolb)

                if stolb-1 >=0:
                    check(stroka+1, stolb-1)
                if stolb+1 < len(poleno[stroka]):
                    check(stroka+1, stolb+1)

            if stolb-1 >=0:
                check(stroka, stolb-1)

            if stolb+1 < len(poleno[stroka]):
                check(stroka,stolb+1)

def isOpen():
    opened = True
    for stroka in pole:
        if '*' in stroka:
            opened = False
    return opened
    if mine.isOpen():
        game = False
                
                    
                       
        






