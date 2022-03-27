import mine

mine.vuvod(mine.pole)

game = True
while game:
    stolb = int(input('Столбик:'))
    stroka = int(input('Строка:'))

    mine.check(stroka - 1, stolb - 1)
    mine.vuvod(mine.pole)
    if mine.isOpen():
        game = False
print('Всё поле открыто!')
