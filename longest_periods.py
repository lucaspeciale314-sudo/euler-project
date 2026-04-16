import sys

def get_period(m):
    if m == 1:
        return ""
    
    remainder = 1
    period_digits = []
    
    # Since m is not divisible by 2 or 5, the decimal expansion 
    # of 1/m is purely periodic. It will always cycle back to remainder 1.
    while True:
        remainder *= 10
        digit = remainder // m
        remainder = remainder % m
        period_digits.append(str(digit))
        
        if remainder == 1:
            break
            
    return "".join(period_digits)

def main():
    try:
        n = int(input("Enter a number n: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
        
    if n < 1:
        print("Please enter a number greater than or equal to 1.")
        return

    results = []
    
    print(f"Calculating periods for numbers up to {n}...")
    
    for m in range(1, n + 1):
        # Exclude numbers divisible by 2 or 5 as requested
        if m % 2 == 0 or m % 5 == 0:
            continue
        
        period = get_period(m)
        if period: # Exclude m=1 which has no period
            results.append((m, period))
            
    # Sort by the length of the period descending
    results.sort(key=lambda x: len(x[1]), reverse=True)
    
    # Get the top 30 longest periods
    top_30 = results[:30]
    
    print("\n--- Top longest periods ---")
    for m, period in top_30:
        # We print: number - period string
        print(f"{m} - {period}")

if __name__ == "__main__":
    main()
