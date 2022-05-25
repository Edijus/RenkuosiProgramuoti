# Task 1
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def is_float(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


def is_number(n):
    if is_integer(n):
        return True
    else:
        return is_float(n)


input1 = input('Įveskite sveikąjį skaičių:')
if is_integer(input1) == False:
    print(input1, 'nėra sveikasis skaičius', type(input1))
    exit(2)

ar_skaicius_teigiamas = int(input1) > 0
print('Skaičius teigiamas:', ar_skaicius_teigiamas)

# Task 2
from datetime import datetime, timedelta
_now = datetime.now()
print('Dabar:', _now)
print('Dabar - 5h:', _now - timedelta(hours=-5))
print('Dabar - 5h:', _now - timedelta(hours=8))
print(_now.strftime('%Y %m %d, %H:%M:%S'))

# Task 3
input2 = input('Įveskite datą ir laiką:')
try:
  entered_date = datetime.strptime(input2, '%Y-%m-%d %H:%M:%S')
except ValueError:
    try:
        entered_date = datetime.strptime(input2, '%Y-%m-%d %H:%M')
    except ValueError:
        try:
            entered_date = datetime.strptime(input2, '%Y-%m-%d')
        except ValueError:
            print('Sakiau įvesti datą...')
            exit(2)

date_diff = entered_date - datetime.now()
days_diff = abs(date_diff.days)
print('Nuo įvestos datos praėjo', int(days_diff / 365), 'metai',
      int(days_diff / 365 * 12), 'mėnesiai',
      days_diff, 'dienų',
      days_diff * 24, 'valandų',
      days_diff * 24 * 60, 'minučių',
      days_diff * 24 * 60 * 60, 'sekundžių')