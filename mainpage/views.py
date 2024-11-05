from django.shortcuts import render
from .models import CustomerComment

# Create your views here.

def index(request):
    return render(request, 'mainpage/index.html') # Render main page index.html.


def homepage(request):
    comments = CustomerComment.objects.filter(is_approved=True).order_by('-comment_date')[:10]  # Fetch last 10 approved comments
    return render(request, 'your_template_name.html', {'comments': comments})