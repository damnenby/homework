from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
# Create your models here.

STATUSES = (
    (1, "Like"),
    (2, "Dislike")
)


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    text = models.TextField(null=True)
    #-1 год к дате создания
    created_at = models.DateTimeField(default=timezone.now()-timezone.timedelta(days=365.24))
    def __str__(self):
        return f"{self.author}'s article"

class Status(models.Model):
    status = models.IntegerField(choices=STATUSES, default=1)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.status} by {self.user.username} article {self.article.id}'


class Comment(models.Model):
    text = models.TextField(default=' ')
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"
