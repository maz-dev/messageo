from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from chat.models import Message

def index(request):
    latest_messages = Message.objects.order_by('-posted')[:5]
    context = {'latest_messages': latest_messages}
    return render(request, 'chat/index.html', context)

