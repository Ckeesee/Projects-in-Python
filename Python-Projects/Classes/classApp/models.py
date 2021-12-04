from django.db import models

# Create your models here.
class djangoClasses(models.Model):

    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default="", blank=True, null=False)
    Insturctor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(default="", blank=True, null=False)


    objects = models.Manager()

    def __str__(self):
        return self.Title