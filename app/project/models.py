from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField()
    tech_stack = models.CharField(max_length=100)
    def __str__(self):
        return self.project_name