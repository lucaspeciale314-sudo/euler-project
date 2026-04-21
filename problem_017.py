# Problem 17
# ugly solution, and I learned it's forty and not fourty.
def counting_word_length(n):
    length=10   #counting from the start "hundred and"
    if n >1000: return 0
    if n == 1000: return 11
    if n == 0: return 4
    
    h=n//100 #count the third digit
    if h == 0: length -= 10
    elif h == 1: length += 3 #3+7
    elif h == 2: length += 3
    elif h == 3: length += 5
    elif h == 4: length += 4
    elif h == 5: length += 4
    elif h == 6: length += 3
    elif h == 7: length += 5
    elif h == 8: length += 5
    elif h == 9: length += 4
    
    n = n%100
    
    if n == 0: return length-3
    elif n ==10: return length+3
    elif n ==11: return length+6
    elif n ==12: return length+6
    elif n ==13: return length+8
    elif n ==14: return length+8
    elif n ==15: return length+7
    elif n ==16: return length+7
    elif n ==17: return length+9
    elif n ==18: return length+8
    elif n ==19: return length+8

    if n%10 == 0: length += 0
    elif n%10 == 1: length += 3
    elif n%10 == 2: length += 3
    elif n%10 == 3: length += 5
    elif n%10 == 4: length += 4
    elif n%10 == 5: length += 4
    elif n%10 == 6: length += 3
    elif n%10 == 7: length += 5
    elif n%10 == 8: length += 5
    elif n%10 == 9: length += 4
    
    n = n//10
    
    if n == 0: return length
    elif n ==2: return length+6
    elif n ==3: return length+6
    elif n ==4: return length+5
    elif n ==5: return length+5
    elif n ==6: return length+5
    elif n ==7: return length+7
    elif n ==8: return length+6
    elif n ==9: return length+6
    
total_sum=0 
for i in range(1,1001):
    total_sum += counting_word_length(i)
print((f"{total_sum}"))
