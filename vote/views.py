import datetime

from django.shortcuts import loader, render, HttpResponse, render_to_response

from vote.models import VoteModel
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

# Create your views here.
def cus(ctx):
    ctx['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return ctx


# @cache_page(10)
@vary_on_headers('User-Agent')
def hello(request, world, offset):
    list = VoteModel.objects.all()
    ctx = cus({"world": '<h1>周超aaaoaiwegaaa为</h1>', 'list': list})

    return render(request, 'hello1.html', ctx)


def helloSession(request):
    list = VoteModel.objects.all()
    ctx = cus({"world": '<h1>周超aaa111111aaa为</h1>', 'list': list})
    print(request.COOKIES)
    print(request.session['fuck'])
    return render(request, 'hello1.html', ctx)


def start_login(request):
    u_name = request.POST['username']
    u_password = request.POST['password']
    user = auth.authenticate(username=u_name, password=u_password)
    if user:
        return render(request, 'login_success.html', {'username': u_name})


def login(request):
    if request.method == 'POST':
        return start_login(request)
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)


def start_regiest(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return render(request, 'login_success.html', {'username': '%s:%s' % ('注册成功', user.username)})
    else:
        return render(request, 'error.html', {'err': form.errors})


def regiest(request):
    if request.method == 'POST':
        return start_regiest(request)
    else:
        return render(request, 'regeist.html')
