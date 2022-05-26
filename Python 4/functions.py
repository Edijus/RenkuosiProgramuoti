def is_leap_year(year: int) -> bool:
    try:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False
    except TypeError:
        print('param should be int')
        return False

def find_leap_year(_from: int, _to: int) -> list:
    leap_years = []
    for year in range(_from, _to + 1):
        if is_leap_year(year):
            leap_years.append(year)

    return leap_years


leap_years = find_leap_year(200, 400)
print(leap_years)
print(is_leap_year('labas'))
