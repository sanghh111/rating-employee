from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField(null=True)
    date_end = models.DateField(null=True)
    tech_stack = models.CharField(max_length=100, null=True )

    created_at = models.DateTimeField(auto_now_add=True, db_column='created_at', blank=True, null=True,
                                      verbose_name=('Created at'))
    updated_at = models.DateTimeField(auto_now=True, db_column='modified_at', blank=True, null=True,
                                      verbose_name=('Updated at'))
    created_by = models.CharField(max_length=100, db_column='created_by', blank=True, null=True, default='',
                                  verbose_name=('Created by'))
    updated_by = models.CharField(max_length=100, db_column='modified_by', blank=True, null=True, default='',
                                  verbose_name=('Updated by'))
    class Meta:
        db_table = "project"
    
    def __str__(self):
        return self.project_name

    