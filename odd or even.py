# Program to check Odd or Even

#num1 = int(input("Enter a number: "))
#num2=int(input("Enter a number:"))
#num3 = int(input("Enter a number: "))
#for num in[num1,num2,num3]:
    #if num % 2 == 0: 
      # print("The number is Even")
#else:
   # print("The number is Odd")

#another way
#num = [5, 4, 9]

#for i in num:
    #if i % 2 == 0:
       # print(i, "is even")
    #else:
        #print(i, "is odd")
#numbers = [45,78,9,5,78,45,78,66,54,22,2,4,6,5,3,2,1]
num=input("enter number separated by space:")
nums=[int(n)for n in num.split()]
even_list = []
odd_list = []

for num in nums:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)  





#by defining a function
def odd_even(nums):
    even_list=[]
    odd_list=[]
    for num in nums:
        if num%2==0:
             
           even_list.append(num)
    else:
        odd_list.append(num)
    return even_list,odd_list
#input
nums=[int(n)for n in input("enter numbers separated by space:").split()]
#call function
even,odd=odd_even(nums)
print("even",even)
print("odd",odd)

#option 4
nums=[list(n) for n in input("enter numbers separtedby space:").split(' ')]

even_list=[]
odd_list=[]
for num in nums:
        if num%2==0:
             
            even_list.append(num)
else:
        
    odd_list.append(num)
print("Even Numbers:", even_list)
print("Odd Numbers:", odd_list)  



