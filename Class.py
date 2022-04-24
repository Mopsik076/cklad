import collections
class Student: 
    def __init__(self, n, nam, a, usp):
        self.name = n
        self.age = a
        self.namber = nam
        self.usp = usp
    def priv(self):
        print('Имя:',self.name,',Возраст:',self.age,',Номер группы:',self.namber,',Успеваемость:',self.usp)
    def mean(self):
        b = self.usp
        mean = 0
        sum = 0
        for i in b:
            sum += i
            mean = sum/len(b)
            #mean_list = [mean]
        return mean
    def search(self):
        answer = True
        for i in self.usp:
            if i == 3 or i == 2:
                answer = False
            else:
                answer = True
        return answer
        
igor = Student(n = 'igor', nam = 3, a = 14, usp = [3,4,2,4,5])
wir = Student(n = 'wir', nam = 1, a = 9, usp = [3,4,2,3,3])
vova = Student(n = 'vova',nam = 4 ,a = 16, usp = [3,3,5,5,5])
dima = Student(n = 'dima',nam = 2 ,a = 5, usp = [4,4,4,4,5])
mark = Student(n = 'mark',nam = 1 ,a = 8, usp = [4,5,4,5,5])

list_of_students = [igor,wir,vova,dima,mark]

list_of_students.sort(key = lambda x: x.mean())

for i in list_of_students:
    i.priv()
    print(i.mean())
print('-----------------------')
for i in list_of_students:
    if i.search() == True:
        i.priv()

