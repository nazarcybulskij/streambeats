from .forms import LoginForm
from django.shortcuts import render
from django.views.generic.edit import FormView


class LoginView(FormView):

    form_class = LoginForm

    template_name = 'account/login.html'

    def get_form_kwargs(self):
        form_kwargs = super(LoginView, self).get_form_kwargs()
        form_kwargs.update({
            'request': self.request    
        })
        return form_kwargs

    def forms_valid(self, form):
        pass

    def forms_invalid(self, form):
        pass
