from django.db import models

# Create your models here.

class Tire(models.Model):
    name = models.CharField(verbose_name=u"Name", max_length=100)
    width = models.IntegerField(verbose_name=u"Width",
                                blank=True, null=True)
    height = models.IntegerField(verbose_name=u"Height",
                                 blank=True, null=True)
    diameter = models.IntegerField(verbose_name=u"Diameter",
                                   blank=True, null=True)
    speed_index = models.CharField(verbose_name=u"Speed index", max_length=100,
                                   blank=True, null=True)
    picture = models.ImageField(u"Picture",
                                upload_to='tiresapp/images/',
                                blank=True, null=True)
