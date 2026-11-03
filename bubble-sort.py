def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for i in range(iter_num):
            print(list)
            if list[i]>list[i+1]:
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
lst=[7,3,1,2,5]
print("sorted array===")
bubblesort(lst)

