from django.shortcuts import render
from django.http import HttpResponse
import random


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def send_message(request):
    messages = ['Winners never quit, quitters never win',
                'If you are not failing, you are not growing',
                'Be the change that you wish to see in the world',
                'I will prepare and some day my chance will come'
                ]
    msg = messages[random.randint(0, 3)]
    return HttpResponse(msg)
