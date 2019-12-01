from django.db import models
# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField(blank = True, null = True)
    sender = models.CharField(max_length = 50)
    url = models.URLField(unique = False, max_length = 50)

    def __str__(self):
        return self.title
