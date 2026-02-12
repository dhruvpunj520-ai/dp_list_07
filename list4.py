import random
lst=[random.randint(1,30) for i in range(50)]
print("The list in : ",lst)
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print("Unique list is: ",new_lst)        
