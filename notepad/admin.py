from django.contrib import admin
from .models import Category, Note, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Note)
