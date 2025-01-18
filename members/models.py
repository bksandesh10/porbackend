from django.db import models



class Members(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    subject = models.CharField(max_length=225)
    message = models.CharField(max_length=225)




def __str__(self):
    return f"{self.name} = {self.email} - {self.subject}"
    