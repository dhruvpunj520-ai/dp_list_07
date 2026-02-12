import random
odd_lst=[]
even_lst=[]
for i in range(5):
    odd_lst.append(random.randrange(1,99,2))
print("Odd numbers list is: ",odd_lst)
for i in range(4):
    even_lst.append(random.randrange(2,100,2))
print("Even numbers list is: ",even_lst)
odd_lst[2]=even_lst
print("Modified list is: ",odd_lst)
flat_lst=[]
for i in range(len(odd_lst)):
    if (isinstance(odd_lst[i],list)):
        for j in range(len(odd_lst[i])):
            flat_lst.append(odd_lst[i][j])
    else:
        flat_lst.append(odd_lst[i])
print("Odd list is: ",flat_lst)
flat_lst.sort()
print("Sorted list is: ",flat_lst)
