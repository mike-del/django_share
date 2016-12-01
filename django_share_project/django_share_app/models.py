from django.db import models

class Mike(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
