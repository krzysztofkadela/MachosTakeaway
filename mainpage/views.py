from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomerCommentForm
from .models import CustomerComment
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.

#def index(request):
#   return render(request, 'mainpage/index.html') # Render main page index.html.
def index(request):
    """Fetch the last 10 approved comments that are updated most recently."""
    comments = CustomerComment.objects.filter(is_approved=True).order_by('-updated_on')[:10]
    return render(request, 'mainpage/index.html', {'comments': comments})  # Render the homepage template with comments

@login_required  # Ensure only logged-in users can access this view
def add_comment(request):
    """View to handle adding a new comment."""
    if request.method == 'POST':
        form = CustomerCommentForm(request.POST)
        if form.is_valid():
            # Create a new comment instance but don't save it to the database yet
            comment = form.save(commit=False)
            comment.user = request.user  # Set the user to the currently logged-in user
            comment.save()  # Save the comment in the database
            return redirect('index')  # Redirect to the homepage or wherever appropriate
    else:
        form = CustomerCommentForm()  # Create an empty form instance

    return render(request, 'add_comment.html', {'comment_form': form})  # Render a page for adding comments (can be a separate template)


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

def user_comments(request):
    # Fetch the last 10 approved comments
    comments = CustomerComment.objects.filter(is_approved=True).order_by('-comment_date')[:10]
    
    return render(request, 'mainpage/usercomment.html', {'comments': comments})