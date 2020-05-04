# Display no. of days in a month

month = int(input("Enter Month [ 1- 12 ] : "))

if month == 2:
    year = int(input("Enter Year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        nodays = 29
    else:
        nodays = 28
elif month in [4, 6, 9, 11]:
    nodays = 30
else:
    nodays = 31

print("No. of days = ", nodays)
