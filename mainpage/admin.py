from django.contrib import admin
from .models import CustomerComment

# Register your models here.

@admin.register(CustomerComment)
class CustomerCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'comment_date', 'updated_on', 'is_approved')  # Display fields including updated_on
    search_fields = ('user__username', 'comment')                      # Enable search by username and comment text
    ordering = ('-comment_date',)                                      # Order comments by date (most recent first)

    # Adding filter options in the admin interface for easy approvals
    list_filter = ('is_approved',)  # Allow filtering comments by approval status