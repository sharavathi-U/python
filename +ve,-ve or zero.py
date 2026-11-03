#option 1 for single number
num=int(input("eneter a number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

#option 2 for multiple numbers




#option 3 using function
def pnz(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return 'zero'
num=int(input('enter a number:'))
result=pnz(num)
print(result)

#option 4 multiple numbers using function
