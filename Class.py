class Student: 
    def __init__(self, n, nam, a, usp):
        self.name = n
        self.age = a
        self.namber = nam
        self.usp = usp
    def priv(self):
        print('Имя:',self.name,',Возраст:',self.age,',Номер группы:',self.namber,',Успеваемость:',self.usp)
    def mean(self):
        a = self.usp
        mean = 0
        sum = 0
        for i in a:
            sum += i
            mean = sum/len(a)
        print('Средняя оценка: ', mean)
        
igor = Student(n = 'igor', nam = 3, a = 14, usp = [3,4,2,4,5])
wir = Student(n = 'wir', nam = 1, a = 9, usp = [3,4,2,3,3])
vova = Student(n = 'vova',nam = 4 ,a = 16, usp = [3,4,2,3,5])
dima = Student(n = 'dima',nam = 2 ,a = 5, usp = [3,2,3,4,5])
mark = Student(n = 'mark',nam = 1 ,a = 8, usp = [3,5,2,5,5])

list_of_students = [igor,wir,vova,dima,mark]

for i in list_of_students:
    i.priv()
    i.mean()


