log = [{'Name':'MopsiK', 'Password':'1234'},{'Name':'Mops', 'Password':'2341'}]

cmd = input('Вход или Регистр: ')
while cmd != 'Выход':
    if cmd == 'Вход':
        logi = input('Name: ')
        pas2 = input('Password: ')
        while not {'Name':logi, 'Password':pas2} in log:
            print('error')
            logi = input('Name: ')
            passw = input('Password: ')
        print('Good')
    elif cmd == 'Регистр':
        login = {input('Name: ')}
        pas = {input('password: ')}
        password = {input('password: ')}
        nash = False
        for slovar in log:
            if slovar['Name'] == logi:
                nash = False
        while pas != password or nash == True:
            
