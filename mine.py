poleno=[['o', 'o', 'f', 'o', 'o', 'f', 'o', 'o', 'o'],
      ['o', 'o', 'f', 'o', 'o', 'f', 'o', 'o', 'o'],
      ['o', 'o', 'f', 'o', 'o', 'f', 'o', 'f', 'o'],
      ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'o', 'o'],
      ['o', 'o', 'f', 'o', 'o', 'o', 'f', 'f', 'f'],
      ['f', 'f', 'f', 'f', 'f', 'f', 'f', 'o', 'o'],
      ['o', 'o', 'f', 'o', 'o', 'o', 'f', 'o', 'o'],
      ['o', 'o', 'f', 'o', 'f', 'o', 'f', 'f', 'f'],
      ['f', 'o', 'f', 'f', 'o', 'o', 'o', 'f', 'o']]


pole=[['*', '*', '*', '*', '*', '*', '*', '*', '*'],
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

def check(stroka, stolb):
    if pole[stroka][stolb]=='*':
        pole[stroka][stolb] = poleno[stroka][stolb]
        if poleno[stroka][stolb]=='o':
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

                
                    
                
        






