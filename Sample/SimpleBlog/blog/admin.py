from django.contrib import admin
from .models import Blog, Tag, Comment, Like

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)
