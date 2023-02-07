from django.db import models

# Create your models here.

class audio_storage(models.Model):

    id = models.AutoField(primary_key = True)
    file_name = models.CharField(max_length = 255)
    my_file = models.FileField()

    def __str__(self):
        return self.file_name


