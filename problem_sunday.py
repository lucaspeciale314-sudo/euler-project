def generate_year_calendar():
    month_starts = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    return month_starts


def concatenate_years():
    years = []
    for year in range(1900, 2023):  # Consider years until 2022
        years.extend(generate_year_calendar())
    return years


def date_to_index(date_str):
    day, month, year = map(int, date_str.split('/'))
    month_starts = generate_year_calendar()
    return month_starts[month - 1] + (day - 1) + (year - 1900) * 365


def count_sundays_on_first():
    sundays_count = 0
    for year in range(1900, 2023):
        index = date_to_index(f'01/01/{year}')
        if index % 7 == 6:  # Checking if it's Sunday
            sundays_count += 1
    return sundays_count
