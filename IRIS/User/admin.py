from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import CustUserCreationForm, CustUserChangeForm
# Register your models here.

class CustUserAdmin(UserAdmin):
    form = CustUserChangeForm
    add_form = CustUserCreationForm

    list_display = ('userName', 'name', 'email', 'roll', 'year', 'department', 'mobileNumber', 'club')
    list_filter = ('is_convener','is_admin')
    
    fieldsets = (
        (None, {'fields': ('userName', 'password')}),
        ('Student info', {'fields': ('email','name','roll','year','department','mobileNumber', 'club',)}),
        ('Permissions', {'fields': ('is_convener','is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'userName', 'name', 'year', 'roll','department','mobileNumber', 'club', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('userName', 'name', 'email', 'roll', 'year', 'department', 'mobileNumber', 'club',)
    ordering      = ('userName', 'name', 'email', 'roll', 'year', 'department', 'mobileNumber', 'club',)
    filter_horizontal = ()


admin.site.register(User, CustUserAdmin)
# admin.site.register(Car)
# admin.site.register(User)