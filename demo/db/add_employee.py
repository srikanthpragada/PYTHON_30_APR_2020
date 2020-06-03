import sqlite3

con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
cur = con.cursor()

# Take input from user
name = input("Enter name :")
job = input("Enter job :")
salary = input ("Enter salary :")

# Execute INSERT command
cur.execute("insert into employees(fullname,job,salary) values(?,?,?)", (name,job,salary))
con.commit()
print("Successfully added employee!")
cur.close()
con.close()

