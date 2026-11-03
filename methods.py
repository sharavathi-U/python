# types of methods
#1.instance methods
#2.class methods
#3.static methods

#instance methods

'''class Subject:
    sub='python'
    def __init__(self):
        print('Initalisation')
    def modify(self):
        self.sub='Machine learning'
        print(self.sub)
s1=Subject()
s1.modify()

s2=Subject()
s2.modify()'''

#instance method i get() and set()
'''class Subject:
    sub = 'python'

    def __init__(self):
        self.sub = 'None'

    def setsub(self, sub):
        self.sub = sub

    def getsub(self):
        return self.sub


s1 = Subject()
s2 = Subject()

s1.setsub("machine learning")
print(s1.getsub())

s2.setsub("AI")
print(s2.getsub())'''
#class method

class Subject:
    sub = 'python'

    def __init__(self):
        print('Initialization')

    @classmethod
    def book(cls):
        cls.name = 'Machine Learning'
        print(cls.name, 'is easy to understand')


Subject.book()

