from django.db import models

class Post(models.Model):
    Sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=140)
    timestamp = models.DateTimeField(blank=True)
    content = models.TextField()

    def __str__(self):
        return "Posted by" + self.author + '_' + self.title