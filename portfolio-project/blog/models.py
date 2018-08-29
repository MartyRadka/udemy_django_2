from django.db import models
from datetime import datetime
from django.db.models import DateTimeField

class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateTimeField(default=datetime.now, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def publication_date_custom(self):
        """Return customized date"""
        return self.publication_date.strftime('%B %-d %Y')

    def summary(self):
        """Return only fist 100 lettres from text"""
        return self.text[:100]
