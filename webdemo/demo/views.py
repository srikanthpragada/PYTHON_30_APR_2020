from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


def about(request):
    return render(request, 'about.html',
                  {'trainer' : 'Srikanth Pragada',
                   'location' : 'Srikanth Technologies'})

def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\apr30\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    con.close()
    return render(request,'list_employees.html', {'employees' : employees})