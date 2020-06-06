from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3


def about(request):
    return render(request, 'about.html',
                  {'trainer': 'Srikanth Pragada',
                   'location': 'Srikanth Technologies'})


def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': employees})


def add_employee(request):
    if request.method == "POST":
        # Take data sent from HTML form
        fullname = request.POST['fullname']
        job = request.POST['job']
        salary = request.POST['salary']
        # Add to EMPLOYEES table
        con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
        cur = con.cursor()
        cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                    (fullname, job, salary))
        con.commit()
        con.close()
        return redirect("/demo/employees")
    else:  # GET request
        return render(request, 'add_employee.html')
