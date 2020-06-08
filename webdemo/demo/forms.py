import django.forms as forms

class UpdateEmployeeForm(forms.Form):
    # Fields
    id = forms.IntegerField(label="Employee ID", required=True)
    salary = forms.IntegerField(label="New Salary", required=True, min_value=0)
