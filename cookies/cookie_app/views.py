from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookies(request):

    response= HttpResponse("cookie set")
    response.set_cookie('username', 'adnan', max_age=3600)
    return response

def get_cookies(request):
    username=request.COOKIES.get('username')
    if username:
        return HttpResponse("hello ,{username}! welcome")
    else:
        return HttpResponse("no cookies found")


def set_session(request):

    request.session['user_id']=878
    return HttpResponse("Session set")

def get_session(request):
    user_id =request.session.get('user_id')
    if user_id:
        return HttpResponse('USER ID:{user_id}')
    else:
        return HttpResponse("No session found")

