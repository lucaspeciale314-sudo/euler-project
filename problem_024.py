import numpy as np
i=0
LIMIT=1000000
millionth_perm=0
for k in range(1,1):
    if k<1000000000 and len(set(str(k))) == 9 and 0 not in set(str(k)):
        i += 1 
        print(k)
    if len(set(str(k))) == 10: 
        i += 1 
        print(k)
    if i == LIMIT: 
        millionth_perm=k 
        break

print(millionth_perm)
print(set(str(1234560789)))

def inductive_permutation(inductive_list):
    new_inductive_list=[]
    for k in inductive_list:
        for l in range(0,10):
            if l not in k:
                new_inductive_list.append(k+[l])
    return new_inductive_list
digits=[]
for i in range(0,10): digits.append([i])
perm_list=digits
for j in range(1,10): perm_list=inductive_permutation(perm_list)
print(inductive_permutation(digits))
    
    
