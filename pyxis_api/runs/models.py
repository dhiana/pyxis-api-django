from django.db import models


class Runs(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    skips = models.IntegerField(blank=True, null=True)
    fails = models.IntegerField(blank=True, null=True)
    passes = models.IntegerField(blank=True, null=True)
    run_time = models.FloatField(blank=True, null=True)
    artifacts = models.TextField(blank=True, null=True)
    run_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'runs'
        managed = False
