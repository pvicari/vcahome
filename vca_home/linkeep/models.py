from django.db import models
from django.utils import timezone

class Card(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    created_date = models.DateTimeField(default = timezone.now)
    
    def create(self):
        self.created_date = timezone.now
        self.save()

    def __str__(self):
        return self.title
        
