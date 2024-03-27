from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    desription=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now=True)
    author=models.CharField(max_length=25)
    def __str__(self):
        return self.title