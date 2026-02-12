import random
lst=[random.randint(1,100) for i in range(20)]
print("The list is : ",lst)
num =int(input("Enter a number: "))
if(num in lst):
    num_occ=[]
    for i, ele in enumerate(lst):
        if(ele==num):
            num_occ.append(i)
    print(f"occurance of {num} in at position {num_occ}")       
else:
    print("invalid input")
