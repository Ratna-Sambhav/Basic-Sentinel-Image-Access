from django.db import models 
from django.urls import reverse

class Entries(models.Model):
    userName = models.CharField(max_length=200, default=1)
    lat = models.FloatField()
    long = models.FloatField()
    date = models.CharField(max_length=50)

    def __str__(self):
        return 'User-'+self.userName[-10:].replace(' ','')+'_'+str(self.pk)

    def get_absolute_url(self): # new
        return reverse('listDetail', args=[str(self.id)])