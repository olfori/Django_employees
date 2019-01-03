from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth import logout
from django.core.paginator import Paginator

from .models import Employees
from .forms import TableForm, EmployeesForm
from .utils import *


LIM = 50   # how many records on a page

LOGOUT = 'Youve been logged out'
NO_USER = 'There is no such user'
LOGIN = 'Yo can authorize. login: admin  pass: 12345678'
NO_LOGIN = 'You are not autorized. login: admin  pass: 12345678'

EMP_DEL = 'The employee record is deleted'
ID_LESS = 'Unable to delete employee record with id<1111'
NEW_REC = 'New record was created'
FIELDS = 'Please, fill the name and the chief id fields'
WAS_UPDATE = 'Record was update'

def emp_tree(request, template_name='tree/emp_tree.html'):

    if request.method == 'GET':
        emps = Employees.objects.filter(level__lte=1)
        emps = emps.order_by('-rght').all()
        count_all = Employees.objects.count()
        data = {
            'employees': emps,
            'count_all': count_all
        }
        return render(request, template_name, context=data)


def emp_table(request, template_name='tree/emp_table.html'):

    if request.user.is_authenticated:

        last_sort_by('id')
        emps = Employees.objects.order_by('id').all()  # id sorting
        p = Paginator(emps, LIM).get_page(1)
        ss_form = TableForm()
        emp_form = EmployeesForm()
        form_names = zip(ss_form, ['id', 'Full name', 'Position', 'Started', 'Salary'])
        emp_photo_url = Employees.objects.get(id=1).photo.url
        data = {
            'employees': p,
            'form_names': form_names,
            'form': ss_form,
            'emp_form': emp_form,
            'url': emp_photo_url,
            'page': p
        }
        return render(request, template_name, context=data)
    else:
        template_name = 'tree/not_authenticated.html'
        data = {
            'text': NO_LOGIN
        }
        return render(request, template_name, context=data)


def logout_(request, template_name='tree/not_authenticated.html'):

    logout(request)
    data = {
        'text': LOGOUT
    }
    return render(request, template_name, context=data)


def not_authenticated(request, template_name='tree/not_authenticated.html'):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('emp_table_url'))   # success page
        else:
            data = {
                'text': NO_USER
            }
            return render(request, template_name, context=data)
    else:
        data = {
            'text': LOGIN
        }
        return render(request, template_name, context=data)

@csrf_protect
def get_empl_photo(request):

    if request.method == 'POST':
            emp_id = request.POST['empl_photo_url']
            emp_photo_url = Employees.objects.get(id=emp_id).photo.url
            data = {
                'url': emp_photo_url
            }
            return JsonResponse(data)
        
    return render(request, "404.html")


@csrf_protect
def ajax_dragdrop(request):
    
    if request.method == 'POST':
        
        print(request.POST)
        id = request.POST['id']
        new_parent_id = request.POST['new_parent']
        new_parent = Employees.objects.get(id=new_parent_id)
        emp = Employees.objects.get(id=id)
        old_par_id = emp.parent_id
        old_par = Employees.objects.get(id=old_par_id)
        childrens_count = old_par.get_children().count()
        emp.move_to(new_parent)
        return JsonResponse({'old_par_id': old_par_id, 'childrens_count': childrens_count})
        
    return render(request, "404.html")


@csrf_protect
def ajax_tree(request):

    if request.method == 'POST':

        id = request.POST['id']
        emps = Employees.objects.filter(parent_id=id).all()

        return json_data_tree(emps)

    return render(request, "404.html")  # if some one try to get to the page


@csrf_protect
def ajax_table(request):

    if request.method == 'POST' and request.user.is_authenticated:
        server_response = ''
        emps = Employees.objects
        print(request.POST)
        print(request.FILES)

        if 'del' in request.POST:
            del_id = int(request.POST['del'])   # deleted object id
            del_obj = emps.get(id=del_id)       # remote object itself
            if del_id > 1111:
                del_obj.delete()
                server_response = EMP_DEL
            else:
                server_response = ID_LESS

        if 'create' in request.POST:
            bound_form = EmployeesForm(request.POST, request.FILES)
            if bound_form.is_valid:
                bound_form.save()
                server_response = NEW_REC
            else:
                server_response = FIELDS

        if 'update' in request.POST:
            emp_id = request.POST['update']
            emp = emps.get(id=emp_id)
            bound_form = EmployeesForm(request.POST, request.FILES, instance=emp)
            if bound_form.is_valid:
                bound_form.save()
                server_response = WAS_UPDATE
            else:
                server_response = FIELDS

        if 'search' in request.POST:        # if search button was pressed
            search = request.POST['search']     # which field to serch
            emps = eval('emps.filter(' + search + '__icontains=request.POST[search])')

        if 'sort_by' in request.POST:       # if sort_by button was pressed
            sort_by = request.POST['sort_by']  # memorized the sort field

            if sort_by[0] == '-':           # if sort field start with '-'
                search = sort_by[1:]        # delete '-'
            else:
                search = sort_by            # by which field of the model to search

            if request.POST[search]:        # if the searh field is not empty
                emps = eval('emps.filter(' + search + '__icontains=request.POST[search])')
            emps = emps.order_by(sort_by).all()   # Sort by value of the 'sort_by' variable
            last_sort_by(sort_by)
        else:
            emps = emps.order_by(last_sort_by()).all()

        page = int(request.POST['page'])
        p = Paginator(emps, LIM)
        p = p.get_page(page)
        return json_data_table(p, server_response)

    return render(request, "404.html")      # if someone tryes to get to the page
