from datetime import datetime, timedelta

# Function to count Sundays that fall on the first of the month

def count_sundays(start_date, end_date):
    current_date = start_date
    sunday_count = 0
    
    while current_date <= end_date:
        if current_date.weekday() == 6:  # 6 corresponds to Sunday
            sunday_count += 1
        current_date += timedelta(days=1)

    return sunday_count

# Define the start and end dates
start_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)

# Count the Sundays on the first of the month
sundays_on_first = count_sundays(start_date, end_date)
print(f'Number of Sundays that fell on the first of the month from {start_date.date()} to {end_date.date()}: {sundays_on_first}')