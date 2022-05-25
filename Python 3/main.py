from datetime import datetime, timedelta

cat = {
    'name': 'John'
}
meow_cats = {key: value for key, value in cat.items()}
print(meow_cats)

keys = cat.keys()
values = cat.values()
copy_cat = {key: value for key, value in zip(keys, values)}
print(copy_cat)

has_cat = True
boolean_values = [True, False, True]
words = ['cat', 'car', 'house']
empty_list = []

print('All values are True:', all(boolean_values))
print('At least one value is True:', any(boolean_values))
print('words has elements:', bool(words))
print('list has elements:', bool(empty_list))
print('0 is True', bool(0))
print('25 is True', bool(25))
print('-5 is True', bool(-5))
print('labas is True', bool('labas'))
print('None is True', bool(None))
print('type of has_cat:', type(has_cat))

if isinstance(5.0, float):
    print('Yes, float')

if isinstance(5, int):
    print('Yes, int')

date_now = datetime.now()
print('Now:', date_now, type(date_now))
date_str = date_now.strftime('%Y-%m-%d')
print('date_now to string:', date_str, type(date_str))
print('str to date:', datetime.strptime(date_str, '%Y-%m-%d'))

modified_date = date_now + timedelta(hours=-5, days=2)
print('modify date:', modified_date)

try:
    print(1/'0')
except ZeroDivisionError:
    print('Dalinti iš 0 gali tik Chuck Norris')
except TypeError:
    print('Ne malkas dalini')
finally:
    print('Done')