from django.db import models

# Create your models here.
class Testdata(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    doi = models.TextField(blank=True, null=True)
    incitations = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testdata'