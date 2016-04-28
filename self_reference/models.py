from django.db import models


class SelfReferenceModel(models.Model):
    object_id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey('self')


class ForeignModel(models.Model):
    id = models.AutoField(primary_key=True)
    foreign_id = models.ForeignKey(SelfReferenceModel)
