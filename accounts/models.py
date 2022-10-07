from django.db import models

# Create your models here.

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=16)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

