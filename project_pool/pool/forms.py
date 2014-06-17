from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    permission = forms.ChoiceField(label="Yetkiler",
                                   choices=(("seciniz", "Seciniz"),
                                            ("user", "User"),
                                            ("admin", "Admin")))
