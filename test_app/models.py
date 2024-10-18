from django.db import models

# Create your models here.
class TestUser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.username)