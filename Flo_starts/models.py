from django.db import models

class AcessLog(models.Model):
    class Meta:
        db_table = "my_data"

    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("접속 경로",max_length=50)
