from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("Hello, world. You're at the poll index.")

from django.shortcuts import render

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all()
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def abhinav(request):
	return HttpResponse("Hello Abhinav")