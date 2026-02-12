import random
lst=(random.randint(-100,100) for i in range(30))
print("The list is : ",lst)
lst_p=[]
lst_n=[]
for i in lst:
    if (i<0):
        lst_n.append(i)
    elif(i>0):
        lst_p.append(i)
    else:
        print("invalid input")
print("List of positive integers",lst_p)
print("List of negative integers",lst_n)

        
        
