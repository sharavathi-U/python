'''def greet():
    print("Hello,Good morning!!!")
greet() '''

#
'''def marriage(boy,girl):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")
marriage("yash","radhika")

marriage("puneeth","ashwini")'''


#default parametes
'''def marriage(boy="yash",girl="radhika"):
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} married {girl}")
marriage( )#default'''

#local and globL VARIABLE

'''def func():
    x="YASH"#local variable
    print("Hello world")
    print(y)
y="radhika"#GLOBAL VARIABLE


print(y)'''

def squares(x):
    return x*x
def cubes(x):
    return x*x*x

lst=[1,2,3,4,5,6]
print(lst)

print(list(map(squares,lst)))
print(list(map(cubes,lst)))