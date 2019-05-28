from django.db import models

# Create your models here.


class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(name='zc')


class VoteModel(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=512)
    sex = models.IntegerField()
    age = models.IntegerField()
    vote_count = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.name


class VotePeople(models.Model):
    vote_who = models.ManyToManyField(VoteModel, verbose_name="投票给")
    key = models.CharField(max_length=20)
    date_time = models.DateTimeField(null=True, blank=True, verbose_name='投票时间')
