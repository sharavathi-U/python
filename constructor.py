# default constructor

'''class subject:
    book = 'python'

    def disp(self):
        print(self.book, 'is easy')

s = subject()
s.disp()'''

#non parameteried constructor

'''class subject:
    book = 'python'

    def __init__(self):
        self.name = 'machine learning'

    def disp(self):
        print(self.book, 'is easy')
        print(self.name,'is easy to learn')

s = subject()
s.disp()'''

#parameterised constructor
class subject:
    book = 'python'

    def __init__(self,sub):
        self.name = sub

    def disp(self):
        
        print(self.name,'is easy to learn')

s = subject( 'Artificial intelligence')
s.disp()

p=subject('datascience')#p=instance of a object
p.disp()

