from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def khoj(request):

    if request.method == "POST":
        # if user post number list and search value
        number_list = request.POST.get("numbers").replace(" ", "")
        search_number = request.POST.get("search").replace(" ", "")
        number_list = number_list.split(",")

        # test user entered valid input by converting to int list
        try:
            number_list_int = list(map(int, number_list))
        except Exception as e:
            message = "invalid Input, Please enter integer and comma only"
            print(e)
            return render(
                request,
                "khoj_the_search/khoj.html",
                {"result": message, "post": True}
            )

        number_list.sort()
        result = False
        if search_number in number_list:
            result = True
        return render(
            request,
            "khoj_the_search/khoj.html",
            {"result": result, "post": True}
        )

    return render(request, "khoj_the_search/khoj.html")
