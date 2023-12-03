import random
even=[]
odd=[]
d={}
for i in range(10):
    rn=random.randint(1,50)
    if rn%2==0:
        even.append(rn)
    else:
        odd.append(rn)
d["even"]=even
d["odd"]=odd
print(d)