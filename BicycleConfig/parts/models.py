from django.db import models
from django.db.models.functions import datetime as dt
from django.utils import timezone



class Parts(models.Model):
    Parts_name = models.CharField(max_length=32,)
    Parts_price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    Parts_description = models.CharField(max_length=260)
    start_date = models.DateTimeField(default=dt.datetime.now(tz=timezone.utc), blank=False)
    end_date = models.DateTimeField(default=dt.datetime.now(tz=timezone.utc), blank=False)

    class Meta:
        db_table = "parts"

