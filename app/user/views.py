from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.views.generic.edit import CreateView

from user.forms import LoginForm, UserRegForm


def login(request):
    """Render Login Template"""

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            # log in user
            # passing email to username because of our custom user model
            # django auth method use username and pass to authenticate
            user = auth.authenticate(
                username=data["email"], password=data["password"])

            # if authentication succeeded
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            # return redirect('login')
            data = {
                "message": "Please check your Email address and password",
                "form": form
            }
            return render(request, "user/login.html", data)

        data = {
            "message": "Invalid Input",
            "form": form,
        }
        return render(request, "user/login.html", data)

    form = LoginForm()

    return render(request, "user/login.html", {"form": form})


def logout(request):
    """Log Out User"""
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    return redirect('home')


class RegistrationView(CreateView):
    """Renders Registration page and create user model"""

    template_name = "user/register.html"
    form_class = UserRegForm

    def get_success_url(self) -> str:

        return reverse('login')
