from datetime import date
now = date.today()
print(type(now));
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(now)
birthday = date(1964, 7, 31)
age = now - birthday
print(type(age))