from django.db import models

# Create your models here.

class LandDetails(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)


class ETRS(models.Model):
    tree_id = models.ForeignKey(LandDetails, on_delete=models.CASCADE)
    tree_name = models.CharField(max_length=200)

class CTRS(models.Model):
    rree_id = models.ForeignKey(LandDetails, on_delete=models.CASCADE)
    tree_name = models.CharField(max_length=200)