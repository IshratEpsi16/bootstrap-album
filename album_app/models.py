from django.db import models

# Create your models here.
class album_db(models.Model):
    image = models.ImageField(upload_to='album/photo/')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.description
class album_db2(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album/photo2/')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.name
    
