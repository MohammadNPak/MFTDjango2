from django.db import models
from django.urls import reverse

from django.conf import settings

settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"Post(id={self.id}) -> {self.title}"
    
    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={"pk": self.pk})
    
