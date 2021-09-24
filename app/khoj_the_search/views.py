from django.shortcuts import render


def khoj(request):
    return render(request, "khoj_the_search/khoj.html")
