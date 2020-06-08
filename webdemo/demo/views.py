from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
from .forms import UpdateEmployeeForm

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

def update_employee(request):
    if request.method == "GET":
        f = UpdateEmployeeForm()
        return render(request,'update_employee.html', {"form" : f})
    else:  # POST
        f = UpdateEmployeeForm(request.POST)
        if f.is_valid():
            id = f.cleaned_data['id']
            salary = f.cleaned_data['salary']
            con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
            cur = con.cursor()
            cur.execute("update employees set salary = ? where id = ?",  (salary,id))
            if cur.rowcount == 1:
                msg = 'Updated Successfully!'
                con.commit()
            else:
                msg = 'Sorry! Employee Id not found!'

            con.close()
            return render(request, 'update_employee.html', {"form": f, 'message' : msg})
        else:  # invalid data from client
            return render(request, 'update_employee.html',
                   {"form": f, 'message' : 'Please correct errors and resubmit form!'})


