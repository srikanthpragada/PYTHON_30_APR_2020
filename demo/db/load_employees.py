import sqlite3

con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
cur = con.cursor()
count  = 0

with open("employees.txt", "rt") as file:
    for line in file:
        parts = line.split(",")
        if len(parts) < 3:
            continue

        try:
            # Execute INSERT command
            cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                        (parts[0], parts[1], parts[2]))
            count += 1
        except Exception as ex:
            print('Error -->', ex)


con.commit()
print(f"Successfully loaded {count} employees!")
cur.close()
con.close()
