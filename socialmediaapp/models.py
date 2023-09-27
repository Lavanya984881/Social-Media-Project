from django.db import models

class Image(models.Model):
    article_name=models.CharField(max_length=50)
    description=models.CharField(max_length=350)
    image = models.FileField(upload_to='images/')


class Feedback(models.Model):
    name=models.CharField(max_length=50)
    comment=models.CharField(max_length=200)
    