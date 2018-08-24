from django.db import models
from datetime import datetime
from django.db.models import DateTimeField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.title
