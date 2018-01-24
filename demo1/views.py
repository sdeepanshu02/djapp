from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu
from django.contrib.auth.decorators import login_required
from .forms import addMenuForm
from django.shortcuts import redirect
from django.contrib import messages


def index(request):
    return HttpResponse("Hello, world. You're at the backend workshop")

def menu(request):
    return HttpResponse("You are at menu page")

def viewMenu(request):
    menu1 = Menu.objects.all()
    menu_str = ""
    for m in menu1:
        menu_str += m.item_name + " "+ str(m.price)+"<BR>"
    return HttpResponse("All Menu:<BR>"+ str(menu_str))

def viewMenuHTML(request):
    menu1 = Menu.objects.all()
    context = {'menu_list': menu1}
    return render(request, 'menu.html', context)

@login_required(login_url='/demo1/login')
def addmenu(request):
    if request.method == "POST":
        form = addMenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            messages.success(request, 'Menu Submitted Successfully')
            return redirect('addmenu')
    else:
        form = addMenuForm()
        return render(request, 'addMenu.html', {'form': form})
