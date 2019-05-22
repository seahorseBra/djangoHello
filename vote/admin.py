from django.contrib import admin
from vote.models import VoteModel


# Register your models here.
class ShowVoteModel(admin.ModelAdmin):
    list_display = ("name", 'sex', 'age', 'vote_count', 'desc')


admin.site.register(VoteModel, ShowVoteModel)
