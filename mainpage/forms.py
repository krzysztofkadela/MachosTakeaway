from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import CustomerComment

class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login', css_class='btn btn-primary'))

class CustomerCommentForm(forms.ModelForm):
    class Meta:
        model = CustomerComment
        fields = ['comment']  # Include comments from comment moddel