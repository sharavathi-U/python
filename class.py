'''class subject:
    book = 'python'
    
    def __init__(self):
        print("initialisation")
    
    def disp(self):
        print('python is easy')

s1 = subject()
s1.disp()
s2 = subject()
s2.disp()'''

'''print(dir(int))'''

#class with in class
'''class Person:
    def __init__(self):
        self.name = input("Enter a name: ")

    def disp(self):
        print(self.name)

    class Dob:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            print(self.dd, self.mm, self.yy)


# Creating Person object
p = Person()
p.disp()

# Creating inner class object
x = Person.Dob()
x.disp()

# Accessing variables directly
print(x.dd, x.mm, x.yy)'''
#function in a function
'''class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def disp(self):
        print(self.name,self.sal)
class sal_incr:
    def incr(s):
        s.sal=s.sal+s.sal*0.1
        s.disp()
s=Emp('john',10000)
s.disp()

sal_incr.incr(s)  '''     

#another way
'''class Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def disp(self):
        print(self.name,self.sal)
class Name:
    def name(s):
        s.name='yash'
        
class sal_incr:
    def incr(s):
        s.sal=s.sal+s.sal*0.1
        s.disp()
s=Emp('john',10000)
s.disp()
Name.name(s)
sal_incr.incr(s) '''

#method 2
'''cass Emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def disp(self):
        print(self.name,self.sal)
class sal_incr:
    def incr(s):
        s.sal=s.sal+s.sal*0.1
        s.disp()
s=Emp('john',10000)
s.disp()
s.name=input('enter a name u wnt to change:')
sal_incr.incr(s) ''' 

#1.	Create a Book class and create five book objects with different details using methods. 

class book:
    def __init__(self,tittle,authour,price):
        self.tittle=tittle
        self.authour=authour
        self.price=price
    def disp(self):
        print(self.tittle,self.authour,self.price)
b1=book("AI",  "john", 1800)
b2=book("DBMS","rahul",250)
b3=book("ADA", "smith",560)
b4=book("DA",  "virat",850)
b5=book("bio", "yash", 188.89)

b1.disp()
b2.disp()
b3.disp()
b4.disp()
b5.disp()

