from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomerCommentForm
from .models import CustomerComment
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.


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
            if request.user.is_superuser:
                comment.is_approved = True
                messages.success(request, "Your comment has been submitted successfully!")
            else:
                comment.is_approved = False
                messages.info(request, "Your comment has been submitted and is awaiting approval.")
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
                messages.success(request, "You have logged in successfully!")  # Display success message
                return redirect('index')  # Redirect to the homepage
            else:
                messages.error(request, "Invalid username or password.")  # Notify of login failure
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    """Log out the user and redirect to the homepage."""
    logout(request)
    messages.success(request, "You have logged out successfully.")  # Message after logout
    return redirect('index')  # Redirect after logging out

@login_required
def user_comments(request):
    # Fetch the last 10 approved comments
    comments = CustomerComment.objects.filter(user=request.user, is_approved=True).order_by('-comment_date')[:10]
    
    if request.method == 'POST':
        # Handle the form submission
        form = CustomerCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user  # Associate the comment with the logged-in user
            new_comment.is_approved = False  # Keeps comment unapproved if not a superuser
            new_comment.save()
            messages.add_message(
                 request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )
            return redirect('user_comments')  # Redirect to comments page or wherever needed
    else:
        form = CustomerCommentForm()

    return render(request, 'mainpage/usercomment.html', {'form': form, 'comments': comments})

@login_required
def edit_comment(request, comment_id):
    """View to edit an existing comment."""
    comment = get_object_or_404(CustomerComment, id=comment_id, user=request.user)

    if request.method == 'POST':
        form = CustomerCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()  # Save the updated comment to the database
            messages.success(request, "Your comment has been updated successfully!")
            return redirect('index')  # Redirect to the homepage
    else:
        form = CustomerCommentForm(instance=comment)  # Create a form instance with the comment data

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

# Delete comments
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(CustomerComment, id=comment_id, user=request.user)
    comment.delete()
    messages.success(request, "Comment deleted successfully!")
    return redirect('user_comments')  # Redirect to the user comments view