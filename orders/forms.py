from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    firstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'fn'}))
    lastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ln'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pw'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pw'}))