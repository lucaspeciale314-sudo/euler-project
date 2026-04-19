#Problem 009 : Pythagorean triples are of the form (2mn, m^2-n^2, m^2+n^2)
# 1000= 2mn+2m^2  <=> 500=m(m+n) now use m>n>0 => m^2 > 250 => m > sqrt(250) ~ 15.8.  Now m is a divisor of 500, and considering the factorization it has to be m=20 , m+n=25
N=(20**2-5**2)*(2*20*5)*(20**2+5**2)
print(f"The product of the numbers forming the Pythagorean triple is {N}")
