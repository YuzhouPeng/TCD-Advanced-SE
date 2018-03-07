from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def home(request):
    return render(request, template_name='home.html')