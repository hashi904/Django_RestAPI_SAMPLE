from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

#ユーザー生成フォーム
class UserCreationForm(forms.ModelForm):
    username =  forms.CharField(label='UserName', max_length=255,required=True,widget=forms.TextInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'date_of_birth', 'weight', 'height')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

#ユーザー修正フォーム
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'date_of_birth','height', 'weight',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]