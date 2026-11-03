lst=[108,'yash',18,'virat']
print(lst)
lst.append(115)
print(lst)
lst1=['sudeep',81,'rahul',1]
lst.extend(lst1)
lst.pop(4)
print(lst)
lst.copy()
lst.reverse()
print(lst)
lst.insert(3,'rcb')
print(lst)
lst.count('r')
print(lst)
lst.clear()
print(lst)

#progran to find smallest and largest number in lst
lst=[18,33,1,45,10,97]
lst.sort(reverse=True)#decending order
print("-------")
smallest = min(lst)
largest = max(lst)

print("List:", lst)
print("Smallest element:", smallest)
print("Largest element:", largest)

