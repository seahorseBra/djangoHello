from django.shortcuts import render
from vote.models import VoteModel
import datetime

# Create your views here.


def hello(request, offset, world):
    list = VoteModel.objects.all()
    world = 'hello www!' + offset + world
    now = datetime.datetime.now() + datetime.timedelta(days=int(offset))
    time = now
    return render(request, 'hello.html', locals())
