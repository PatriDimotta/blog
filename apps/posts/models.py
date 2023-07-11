from django.db import models

# Create your models here.
class CAtegoria(models.Model):
    nombre= models.CharField(max_length=30, null=False)

    def _str_(self):
        return self.nombre
