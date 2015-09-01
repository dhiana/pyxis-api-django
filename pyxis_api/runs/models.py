from django.db import models


class Run(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    skips = models.IntegerField(blank=True, null=True)
    fails = models.IntegerField(blank=True, null=True)
    passes = models.IntegerField(blank=True, null=True)
    run_time = models.FloatField(blank=True, null=True)
    artifacts = models.TextField(blank=True, null=True)
    run_at = models.DateTimeField(blank=True, null=True)

    def success_percentage(self):
        if self.passes == 0:
            return 0

        total = self.passes + self.skips + self.fails
        percent =  (self.passes / float(total)) * 100
        truncated = int(percent)
        return truncated

    class Meta:
        db_table = 'runs'
