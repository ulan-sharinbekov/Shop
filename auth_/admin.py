from django.contrib import admin
from auth_.models import MyUser
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Profile
# class MyUserAdmin(UserAdmin):
#     model = MyUser
#     list_display = ('username','email', 'is_staff', 'is_active',)
#     list_filter = ('username', 'email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username','email', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
# admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MyUser)
admin.site.register(Profile)
