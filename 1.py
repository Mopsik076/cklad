b = ['1','2','3','4','5','6','7','8','9','0']
a = input('Пароль: ')
def fun(num):
    print('Функция запущена')
    for i in num:
        if i in b:
            c = 0
            print('В пароле есть спецсимвол')
        else:
            print('В пароле нет спецсимвола')

def fun1(num):
    for i in num:
        if i.islower():
            print('В пароле есть строчная буква')
        else:
            print('В пароле нет строчнон буквы')
def fun2(num):
    for i in num:
        if i.isupper():
            print('В пароле есть прописная буква')
        else:
            print('В пароле нет прописной буквы')
        
fun(a)
fun1(a)
fun2(a)
