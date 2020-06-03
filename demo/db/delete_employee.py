import sqlite3

con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
cur = con.cursor()
id = input("Enter Id:")
cur.execute("delete from employees where id = ?", (id,))
if cur.rowcount == 1:
    con.commit()
    print("Deleted successfully!")
else:
    print("Sorry! Employee Id Not Found!")


cur.close()
con.close()
