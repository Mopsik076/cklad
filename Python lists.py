chat = input('Введите команду:').lower()
myList = [1,2,3]
while chat != 'выход':
    if chat == 'показать список':
        print(myList)
        chat = input('Введите команду:').lower()
    if chat == 'добавить':
        myList.append(input('Введите новый элемент:'))
        chat = input('Введите команду:').lower()
    if chat == 'удалить':
        myList.remove(int(input('Введите файл для удаления:')))
        chat = input('Введите команду:').lower()
    if chat == 'редактировать':
        i = input('Введите индекс:')
        myList.pop(int(i))
        myList.insert(int(i), input('Новое значение:'))
        chat = input('Введите команду:').lower()





print('чат-бот закончил')
chat = input('Введите команду:').lower()
