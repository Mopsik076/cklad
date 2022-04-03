slov = {'Имя':'Антон','Возраст':'16','Особенности':'Отличник'}
cmd = input('Действие:').lower()
while cmd != '_':
    if cmd == 'редактор':
        slov['Имя']= input('Имя: ')
        slov['Возраст']= input('Возраст: ')
        slov['Особенности']= input('Особенности: ')
        cmd = input('Действие:').lower()
    if cmd == 'добавить':
        slov [input('Название:')]= input('Значение:')
        cmd = input('Действие:').lower()
    if cmd == 'удалить':
        del slov[input('Название:')]
        cmd = input('Действие:').lower()
    if cmd == 'вывод':
        for key in slov:
            print( '',key,':',slov[key])
        cmd = input('Действие:').lower()
    else:
        cmd = input('Действие:').lower()
cmd = input('Действие:').lower()
