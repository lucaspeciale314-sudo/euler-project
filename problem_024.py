# Problem 24: we use the fact that we can compute artificially the first digit by observing that the smallest 9! 
# permutations will start with 0, the next 9! with 1, etc. etc. 9! = 362 880 and 9! * 2 + 274 240 = 1 000 000.
# This is necessary to have the result in a acceptable time (~1s).
# A better method would be to inductively use the reasoning used to choose '2' to choose the next digits as well.
def inductive_permutation(inductive_list):
    new_inductive_list=[]
    for k in inductive_list:
        for l in range(0,10):
            if l not in k:
                new_inductive_list.append(k+[l])
    return new_inductive_list
digits=[[2]]
#for i in range(0,10): digits.append([i])
perm_list=digits
for j in range(1,10): perm_list=inductive_permutation(perm_list)
print(perm_list[274239])
    
