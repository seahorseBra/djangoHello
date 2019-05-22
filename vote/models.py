from django.db import models


# Create your models here.


class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(name='zc')


class VoteModel(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=512)
    sex = models.IntegerField(max_length=1)
    age = models.IntegerField(max_length=3)
    vote_count = models.IntegerField(max_length=7)
