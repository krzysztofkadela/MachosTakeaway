from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Submit
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
        fields = ['comment']
        labels = {
            'comment': 'Your Thoughts',  # Change 'Your Thoughts' to whatever you want
        }
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Enter your comment here...',
                'class': 'form-control',
                'rows': 3,
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()  # Initialize FormHelper
        self.helper.layout = Layout(
            Field('comment', css_class='form-control'),
            Submit('submit', 'Submit Comment', css_class='btn btn-primary')
        )