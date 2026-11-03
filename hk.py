'''lst=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter a number:"))
if n in lst:
    print(1,n+1)
else:
    print()'''

'''n=int(input())
for i in range(1,n+1):
    print(i)'''

'''n = int(input())
arr = map(int, input().split())
runner_up=arr.sort()
reverse=True
print(runner_up)'''

'''n = int(input().strip())
if n %2!=0:
    print("Weird")
elif n %2==0 and range(2,5):
    print("Not Weird")
elif n %2==0 and range(6,20):
    print("Weird")
else :
    print("Not Weird")'''

'''sharavathi=["yash"]
print(sharavathi)'''

'''def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    print(line)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)'''

'''def print_full_name(first, last):
    print(f"Hell0{first} {last}!You just delved into python." )
    

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)'''

def count_substring(string, sub_string):
    count =0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)]==sub_string:
            count +=1 
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    

    
