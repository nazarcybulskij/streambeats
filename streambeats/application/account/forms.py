from django import forms
from django.contrib import auth


class LoginForm(forms.Form):

    """
        Form for custom authentication...
    """

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        
        """
            Login user on clean action
        """

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = auth.authenticate(
            username = username,
            password = password
        )

        if user:
            auth.login(self.request, user)
        return super(LoginForm, self).clean()
