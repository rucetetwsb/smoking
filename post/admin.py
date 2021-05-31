from django.contrib import admin
from .models import Post, Answer, Comment #comment 추가

# Register your models here.
admin.site.register(Post)
admin.site.register(Answer)

admin.site.register(Comment)