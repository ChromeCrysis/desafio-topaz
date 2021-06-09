from django.db import models

# Create your models here.
class Dado(models.Model):
    id_event = models.AutoField(primary_key=True)
    date_event = models.CharField(max_length=100, null=True, blank=True)
    event_type = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=30, null=True, blank=True)
    user = models.CharField(max_length=150, null=True, blank=True)
    device_id = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.event_type

    class Meta:
        managed= True
        ordering = ['id_event']
        db_table = 'dados'