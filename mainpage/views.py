from django.shortcuts import render
from .models import CustomerComment

# Create your views here.

#def index(request):
#   return render(request, 'mainpage/index.html') # Render main page index.html.


#def homepage(request):
#   comments = CustomerComment.objects.filter(is_approved=True).order_by('-comment_date')[:10]  # Fetch last 10 approved comments
#   return render(request, 'index.html', {'comments': comments})

def index(request):
    # Fetch the last 10 approved comments that are updated most recently
    comments = CustomerComment.objects.filter(is_approved=True).order_by('-updated_on')[:10]
    
    return render(request, 'mainpage/index.html', {'comments': comments})  # Render the homepage template with comments