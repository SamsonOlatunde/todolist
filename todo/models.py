from django.db import models

# Create your models here.
class AddList(models.Model):
    title = models.CharField(max_length=1000, default='')
    

    def __str__(self):
        return self.title