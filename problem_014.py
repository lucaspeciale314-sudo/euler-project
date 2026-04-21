# Problem 14: finding the longest path obtained by the collatz iterative function with start unter 1 000 000. 
# We use a recursive procedure, apparently there is a limit to how much a function can call itself ( 1000 times )
# in this case this isn't relevant as the longest path is 524 steps long.

def recursive_collatz(collatz,n):
    if n in collatz:
        return collatz
    if n % 2 == 0:
        collatz[n]=recursive_collatz(collatz,n//2)[n//2]+1
        return collatz
    else:
        collatz[n]=recursive_collatz(collatz,3*n+1)[3*n+1]+1
        return collatz
        
# By length we consider the number of steps necessary to get to 1
collatz={1:0}
best_start=1
for k in range(2,1000000):
    collatz=recursive_collatz(collatz,k)
    if collatz[k]>collatz[best_start]:
        best_start=k


print(f"the longest path is obtained starting with {best_start} and the length is {collatz[best_start]} ")
