from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

from .forms import CustomerCommentForm, CustomLoginForm
from .models import CustomerComment


def index(request):
    """
    Homepage view, fetching the last 10 approved comments.
    """
    google_maps_api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    comments = CustomerComment.objects.filter(is_approved=True).order_by('-updated_on')[:10]
    
    context = {
        'comments': comments,
        'google_maps_api_key': google_maps_api_key
    }
    return render(request, 'mainpage/index.html', context)


def custom_login(request):
    """Handle user login using CustomLoginForm."""
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully!")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    """Log out the user and redirect to the homepage."""
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('index')


@login_required
def add_comment(request):
    """
    View for adding a new comment.
    If the user is a superuser, the comment is auto-approved.
    Otherwise, it awaits approval.
    """
    if request.method == 'POST':
        form = CustomerCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            # Auto-approve if superuser:
            if request.user.is_superuser:
                comment.is_approved = True
                messages.success(request, "Your comment has been submitted successfully!")
            else:
                comment.is_approved = False
                messages.info(request, "Your comment has been submitted and is awaiting approval.")
            comment.save()
            return redirect('index')
    else:
        form = CustomerCommentForm()
    return render(request, 'add_comment.html', {'comment_form': form})


@login_required
def user_comments(request):
    """
    Display the current user's comments (approved or unapproved).
    Allow user to submit new comments.
    """
    comments = CustomerComment.objects.filter(user=request.user).order_by('-comment_date')
    
    if request.method == 'POST':
        form = CustomerCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            # Keep comment unapproved if not a superuser:
            if request.user.is_superuser:
                new_comment.is_approved = True
                messages.success(request, "Your comment has been submitted successfully!")
            else:
                new_comment.is_approved = False
                messages.info(request, "Comment submitted and awaiting approval.")
            new_comment.save()
            return redirect('user_comments')
    else:
        form = CustomerCommentForm()

    return render(request, 'mainpage/usercomment.html', {
        'form': form,
        'comments': comments
    })


@login_required
def edit_comment(request, comment_id):
    """
    View to edit an existing comment that belongs to the logged-in user.
    After editing, if user is not superuser, mark comment as unapproved.
    """
    comment = get_object_or_404(CustomerComment, id=comment_id, user=request.user)
    
    if request.method == 'POST':
        form = CustomerCommentForm(request.POST, instance=comment)
        if form.is_valid():
            updated_comment = form.save(commit=False)
            
            # If user is not superuser, set is_approved=False
            if not request.user.is_superuser:
                updated_comment.is_approved = False

            updated_comment.save()
            messages.success(request, "Your comment has been updated successfully!")
            return redirect('user_comments')  # or wherever you want
    else:
        form = CustomerCommentForm(instance=comment)
    
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """
    Delete an existing comment if it belongs to the logged-in user.
    """
    comment = get_object_or_404(CustomerComment, id=comment_id, user=request.user)
    comment.delete()
    messages.success(request, "Comment deleted successfully!")
    return redirect('user_comments')