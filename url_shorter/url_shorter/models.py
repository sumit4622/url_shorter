from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class urls(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    long_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        username = self.user.username
        return f"{username} have created the short {self.short_code} -> {self.long_url}"