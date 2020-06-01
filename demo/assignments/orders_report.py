import datetime

with open("orders.txt", "rt") as f:
    orders = []
    for line in f:
        dates = line.strip("\n").split(",")
        if len(dates) < 2:
            continue
        try:
            sd = datetime.datetime.strptime(dates[0], "%d-%m-%Y")
            ed = datetime.datetime.strptime(dates[1], "%d-%m-%Y")
            days = (ed - sd).days   # take days from timedelta
            orders.append((days, sd, ed))  # Add tuple to list
        except:
            pass    # ignore errors

for order in sorted(orders):  # Sort by first element in tuple
    print(f"{order[1].strftime('%d-%m-%Y')} {order[2].strftime('%d-%m-%Y')}  {order[0]:3}")
