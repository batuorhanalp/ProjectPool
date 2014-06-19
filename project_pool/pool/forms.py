from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    name = forms.CharField(label="Ad Soyad")
    email = forms.EmailField(label="Email")
    permission = forms.ChoiceField(label="Yetkiler",
                                   choices=(("seciniz", "Seciniz"),
                                            ("user", "User"),
                                            ("admin", "Admin")))
