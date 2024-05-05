from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

def set_form_field_style(field):
    field.widget.attrs.update({
        'class': 'appearance-none border rounded-lg bg-zinc-300 w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
    })

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'ФИО'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтвердите пароль'
        self.fields['email'].label = 'Почта'
        self.fields['company'].label = 'Компания'
        self.fields['phone'].label = 'Номер телефона'

        for field_name, field in self.fields.items():
            set_form_field_style(field)


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_form_field_style(self.fields['username'])
        set_form_field_style(self.fields['password'])