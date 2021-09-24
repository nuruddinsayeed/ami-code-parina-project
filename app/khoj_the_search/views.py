from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def khoj(request):
    return render(request, "khoj_the_search/khoj.html")
