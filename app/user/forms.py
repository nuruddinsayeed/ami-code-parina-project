from django import forms
from django.contrib.auth import get_user_model


class UserRegForm(forms.ModelForm):
    """Djanog Form for Custom User Registration"""

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        """Here We setup Our custom Form"""

        model = get_user_model()
        fields = [
            'name',
            'email',
            'password',
        ]

        # Customize defautl Labels
        labels = {
            'name': "Name",
            'Email': 'Email Address',
            'password': 'Password'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
        }

        error_messages = {
            "email": {
                "required": "email Can not be Empty",
            },
        }

    def save(self, commit=True):
        """Overriding save method as we need to user our custom user
        password encription method"""
        user = super().save(commit=False)
        password = user.password
        user.set_password(password)  # use custom user pass encription
        if commit:
            user.save()
        return user

    # Overriding clean funciton to add client site pass check validation
    def clean(self):
        cleaned_data = super(UserRegForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error("confirm_password", "Passwords doesn't match")


class LoginForm(forms.Form):
    """Create django login form"""

    email = forms.CharField(
        max_length=150,
        label="Enter Your Email",
        required=True,
        error_messages={
            "required": "Email Can not be empty",
        },
        widget=forms.EmailInput(
            attrs={'placeholder': 'email', 'class': 'form-control'}),
    )

    password = forms.CharField(
        max_length=255,
        label="Enter Your Password",
        required=True,
        error_messages={
            "required": "Password Can not be empty",
            "max_length": "Please Enter a Shorter Password"
        },
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
