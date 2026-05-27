LIMIT=1001
half_length=LIMIT//2
sum=0
for i in range(1,LIMIT+1):
    sum=sum+i*i
sum += half_length
sum=2*sum-1-2*(half_length+1)*half_length
print(sum)
