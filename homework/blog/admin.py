from django.contrib import admin
from .models import Article, Status, Author, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Status)
admin.site.register(Author)
admin.site.register(Comment)