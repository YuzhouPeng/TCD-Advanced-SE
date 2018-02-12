from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=100)
    password = forms.CharField(label="密码", min_length=3, max_length=50, widget=forms.PasswordInput)