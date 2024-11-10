from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import CustomerComment
from .forms import CustomLoginForm

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

def custom_login(request):
    """Handle login with CustomLoginForm."""
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the homepage
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    """Log out the user and redirect to the homepage."""
    logout(request)
    return redirect('index')  # Redirect after logging out

#def search_view(request):
#   query = request.GET.get('q')  # Assuming the search form uses a parameter 'q'
#   results = []  # Populate this with actual search results based on your logic
#  return render(request, 'search_results.html', {'results': results})  # Point to your template