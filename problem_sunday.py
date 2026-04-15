def is_leap(year: int) -> bool:
    """Return True if year is a leap year."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month: int, year: int) -> int:
    """Return the number of days in the given month of the given year."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        raise ValueError("Invalid month")


def generate_calendar(year: int):
    """
    Generate the list of all days of the year.
    True means the day is the first of a month, False otherwise.
    """
    calendar = []
    for month in range(1, 13):
        for day in range(1, days_in_month(month, year) + 1):
            calendar.append(day == 1)
    return calendar


def total_days_from_1900(day: int, month: int, year: int) -> int:
    """
    Return the absolute day number starting from 01/01/1900 = 1.
    """
    total = 0

    for y in range(1900, year):
        total += len(generate_calendar(y))

    for m in range(1, month):
        total += days_in_month(m, year)

    total += day
    return total


def valid_date(day: int, month: int, year: int) -> bool:
    """Check whether a date is valid and not before 01/01/1900."""
    if year < 1900:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    return True


def count_sundays_on_first_between(d1: int, m1: int, y1: int, d2: int, m2: int, y2: int) -> int:
    """
    Count how many Sundays fell on the first of the month
    between the two dates inclusive.
    """
    start_total = total_days_from_1900(d1, m1, y1)
    end_total = total_days_from_1900(d2, m2, y2)

    count = 0

    for y in range(y1, y2 + 1):
        cal = generate_calendar(y)
        year_start_total = total_days_from_1900(1, 1, y)

        for i in range(len(cal)):
            absolute_day_number = year_start_total + i

            if start_total <= absolute_day_number <= end_total:
                if cal[i] and absolute_day_number % 7 == 0:
                    count += 1

    return count


def read_date(message: str):
    """Read a date in DD/MM/YYYY format."""
    date_str = input(message)
    day, month, year = map(int, date_str.split("/"))
    return day, month, year


def main():
    try:
        d1, m1, y1 = read_date("Insert the start date (DD/MM/YYYY): ")
        d2, m2, y2 = read_date("Insert the end date (DD/MM/YYYY): ")
    except ValueError:
        print("Invalid format. Use DD/MM/YYYY.")
        return

    if not valid_date(d1, m1, y1) or not valid_date(d2, m2, y2):
        print("One or both dates are invalid.")
        return

    if total_days_from_1900(d1, m1, y1) > total_days_from_1900(d2, m2, y2):
        print("The start date must be earlier than or equal to the end date.")
        return

    result = count_sundays_on_first_between(d1, m1, y1, d2, m2, y2)
    print("Number of Sundays falling on the first of a month:", result)


main()
