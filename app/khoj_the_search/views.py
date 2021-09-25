from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core.models import UserInputValue


def save_numb_list(user, number_list):
    """Save search list to the database"""

    # converting list to string to store it in our database as string (text)
    sorted_nums_string = ", ".join([str(arg) for arg in number_list])
    num_sting = UserInputValue.objects.create(
        user=user, input_values=sorted_nums_string)
    num_sting.save()


@login_required(login_url='login')
def khoj(request):
    """Render Khoj the serch page"""

    if request.method == "POST":
        number_list = request.POST.get("numbers").replace(" ", "")
        search_number = request.POST.get("search").replace(" ", "")
        number_list = number_list.split(",")

        # test user entered valid input by converting to int list
        try:
            number_list_int = list(map(int, number_list))
            search_number_int = int(search_number)
        except Exception as e:
            message = "invalid Input, Please enter integer and comma only"
            print(e)
            return render(
                request,
                "khoj_the_search/khoj.html",
                {"result": message, "post": True}
            )

        number_list_int.sort(reverse=True)

        # save the validated data
        save_numb_list(request.user, number_list_int)

        result = False
        if search_number_int in number_list_int:
            result = True
        return render(
            request,
            "khoj_the_search/khoj.html",
            {"result": result, "post": True}
        )

    return render(request, "khoj_the_search/khoj.html")
