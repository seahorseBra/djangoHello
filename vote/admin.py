from django.contrib import admin
from vote.models import VoteModel, VotePeople


# Register your models here.
class ShowVoteModel(admin.ModelAdmin):
    list_display = ("name", 'sex', 'age', 'vote_count', 'desc')
    fields = ("name", 'vote_count', 'sex', 'age', 'desc')


class ShowVotePeopleModel(admin.ModelAdmin):
    list_display = ('key', 'date_time')
    list_filter = ('date_time',)
    date_hierarchy = 'date_time'
    ordering = ('-date_time',)
    raw_id_fields = ('vote_who',)
    filter_horizontal = ('vote_who',)


admin.site.register(VoteModel, ShowVoteModel)
admin.site.register(VotePeople, ShowVotePeopleModel)
