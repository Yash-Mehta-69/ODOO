from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Exams(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.DateField()
    examiner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    invigilator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField()

    def __str__(self):
        return self.text