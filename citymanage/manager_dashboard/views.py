from django.shortcuts import render
from django.shortcuts import redirect
from manager_dashboard import models
from manager_dashboard import form
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required(login_url='/login')
def index(request):
    pass
    return render(request, 'index.html')


def register(request):
    pass
    return render(request, 'index.html')


def logout(request):
    pass
    return redirect("/index/")

def home(request):
    pass
    return render(request, 'index.html')

def contact(request):
    pass
    return render(request, 'contact.html')

def monitor(request):
    pass
    return render(request, 'monitor.html')

def login(request):
    if request.method == "POST":
        login_form = form.UserForm(request.POST)
        message = "Please check the imput of username/password"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    message = "Password incorrect"
            except:
                message = "Non-exist user"
        return render(request, 'login.html', locals())

    login_form = form.UserForm()
    return render(request, 'login.html', locals())