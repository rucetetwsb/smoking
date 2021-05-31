from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    number = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        permissions = [
            ('can_answer', 'Can Answer')
        ]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.number.__str__()
        return self.title
        return self.text

class Answer(models.Model):
    number = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text

# Post와 1:n관계인 Comment
# class Comment(models.Model):
#     post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     comment_text=models.TextField()
#     created_at=models.DateTimeField(default=timezone.now)
#
#     def approve(self):
#         self.save()
#
#     def __str__(self):
#         return self.comment_text

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)