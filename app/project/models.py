from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    tech_stack = models.CharField(max_length=100, null=True )
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.project_name

    