import webbrowser
list1 = []
class St:
    def __init__(self, name, age):
        self.name = name
        self.age = age
cmd = input('Действие: ')
while cmd != 'выход':
    if cmd == 'google':
        webbrowser.open('https://www.google.ru/')
        cmd = input('Действие: ').lower()
    if cmd == 'youtube':
        webbrowser.open('https://www.youtube.com/')
        cmd = input('Действие: ').lower()
    if cmd == 'list':
        listcmd = input('Действие со списком: ')
        if listcmd == 'добавить':
                list1.append(str(input('Элемент: ')))
                listcmd = input('Действие со списком: ').lower()
        if listcmd == 'список':
                print(list1)
                listcmd = input('Действие со списком: ').lower()
        if listcmd == 'удалить':
                list1.remove(str(input('Элемент: ')))
                listcmd = input('Действие со списком: ').lower()
        if listcmd == 'отмена':
                cmd = input('Действие: ').lower()
    if cmd == 'class':
        you = St(name =(input('Имя: ')), age =(input('Возраст: ')))
        
