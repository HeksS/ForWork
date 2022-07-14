import row as row
from django.shortcuts import render, redirect
from django.db import connection
from .models import Staf, Role
from .forms import RoleForm, UsersForm
from django.views.generic import DetailView, UpdateView


# Create your views here.
# Страничка сотрудников
def index(request):
    people = Staf.objects.all()
    return render(request, 'forwork/Main.html', {'people': people})

# получаем детали сотрудника
class DetailStaf(DetailView):
    model = Staf
    template_name = 'forwork/stafdetail.html'
    context_object_name = 'staf'

# Обновляем данные сотрудника
class StafUpdate(UpdateView):
    model = Staf
    template_name = 'forwork/CreateUsers.html'

    form_class = UsersForm


def Roles(request):
    role = Role.objects.all()
    return render(request, 'forwork/Roles.html', {'role': role})

class RoleUpdate(UpdateView):
    model = Role
    template_name = 'forwork/CreateR.html'

    form_class = RoleForm
# функция добавления роли
def createRole(request):
    error = ''
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Roles')
        else:
            error = 'Ошибка'

    form = RoleForm()

    data = {
        'form': form
    }
    return render(request, 'forwork/CreateR.html', data)

#функция добавления сотрудника
def createUsers(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'

    form = UsersForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'forwork/CreateUsers.html', data)
