import sqlite3

con = sqlite3.connect(r"c:\classroom\apr6\hr.db")
cur = con.cursor()
id = input("Enter Id:")
salary = input("Enter salary :")

cur.execute("update employees set salary = ? where id = ?", (salary, id))

if cur.rowcount == 1:
    print("Updated successfully!")
else:
    print("Sorry! Employee Id Not Found!")

con.commit()
cur.close()
con.close()
