from django.db import models


class SelfReferenceModel(models.Model):
    object_id = models.AutoField()
    parent_id = models.ForeignKey('self')
    
