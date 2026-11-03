#print(range(10))
'''print(range(1,5))
r=range(1,5)
for i in r:
    print(i)
r=range(30,20,4)
print(r)
for i in r:
    print(i)

print(list(range(1,5)))
print(list(range(1,10,2)))
print(list(range(-10,0)))

r1=range(1,10,)

print(r1.index(1))
print(r1[5])

r=range(1,5)
for i in r:
    print("4*",i,"=",i*4)'''
# for single number
'''num=int(input("enter a number:"))
r=range(1,11)
for i in r:
    print(num,"*",i,"=",num*i)'''
#for single number
'''def multi(num):

    for i in range(1,11):
        print(num,"*",i,"=",num *i)
    return num
num=int(input("enter a number:"))
num=multi(num)'''


#for two numbers

'''num1,num2=[float(num)for num  in input('enter a number separated  by spaces :').split( )]

for i in range(1,11):
     print(num1,"*",i,"=",num1*i)
print("----------------------------------------")
for i in range(1,11):
     print(num2,"*",i,"=",num2*i)'''
    
 ##using functions 
'''def multi_table(num):
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)

num1,num2= [int(num) for num in input("Enter numbers separated by spaces: ").split()]


multi_table(num1)

print("----------------------------------------")

multi_table(num2)'''

# for multiple i.e range from(2 to 5)

'''start=int(input("enter the number:"))
end=int(input("enter end number:"))
for num in range(start,end+1):
    print("------------------------------")
    
    for i in range(1,11):
        print(num,"*",i,"=",num*i)'''

# using functions
def tables(start, end):
    for num in range(start, end + 1):

        print("---------------------------------")
        for i in range(1, 11):
            print(num, "*", i, "=", num * i)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

tables(start, end)

