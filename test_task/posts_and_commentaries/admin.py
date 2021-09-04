"Модуль, в котором регистрируются модели БД в панели администратора"
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
