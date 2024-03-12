from django.contrib import admin
from .models import User
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass