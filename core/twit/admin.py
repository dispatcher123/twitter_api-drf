from django.contrib import admin
from .models import Profile,Twitter,Comment
# Register your models here.


@admin.register(Profile)
class Profileadmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','email','phone')


@admin.register(Twitter)
class Twitteradmin(admin.ModelAdmin):
    list_display=('twit','updated_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('profiles','twitter','created_date','updated_date')
