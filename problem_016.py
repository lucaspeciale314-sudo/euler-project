# Problem 16
n=2**1000
digits=[int(k) for k in str(n)]
sum=0
for k in digits:
    sum += k

print(f"{sum}")
# Is there a smarter way?
