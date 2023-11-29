from django.db import models

# makemigrations - create changes and store it in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=130)
    feedback = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name