from django import forms

from .models import Employees


class TableForm(forms.Form):
    id = forms.CharField(max_length=50, required=False)
    name = forms.CharField(max_length=50, required=False)
    position = forms.CharField(max_length=50, required=False)
    emp_date = forms.CharField(max_length=50, required=False)
    salary = forms.CharField(max_length=50, required=False)
    photo = forms.FileInput()

    id.widget.attrs.update({'class': 'form-control shadow-none'})
    name.widget.attrs.update({'class': 'form-control shadow-none'})
    position.widget.attrs.update({'class': 'form-control shadow-none'})
    emp_date.widget.attrs.update({'class': 'form-control shadow-none'})
    salary.widget.attrs.update({'class': 'form-control shadow-none'})


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'position', 'salary', 'parent', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'position': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
            'parent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Chief id'}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Photo'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeesForm, self).__init__(*args, **kwargs)
        self.fields['parent'].required = True
        
    def clean(self):
        cleaned_data = super(EmployeesForm, self).clean()
        print(cleaned_data)
