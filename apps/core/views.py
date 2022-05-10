from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import messageForm
from .models import message
import logging
import secrets
from .IA import OpenIA
import asyncio

# Create your views here.

def home(request,token=''):
    template_name ='core/home.html'
    if not request['token']:
        token = secrets.token_hex(16)
    context = {
        'token': token
    }
    return render(request, template_name, context)

def returning(request,data):
    if request.method == 'POST':
        msgForm = OpenIA.Interation(data['token'])
        logging.warning(msgForm)
        return msgForm

def sending(request):
    template_name = 'core/home.html'
    context = {}
    if request.method == 'POST':
        logging.warning(request.POST)
        token = request.POST['token']
        if token == '':
            token = secrets.token_hex(16)
        data = {
            'mensagem' : request.POST['mensagem'],
            'token' : token,
            'is_human' : True 
        }
        logging.warning(data)
        form = messageForm(data)
        if form.is_valid():
            form.save()
            returning(data=data,request=request)
            messageobj = message.objects.filter(token=token).values('mensagem','is_human')
            context['token'] = token
            context['mensagens'] = messageobj
        return render(request, template_name, context)

def home(request):
    template_name ='core/home.html'
    context = {
        'token' : secrets.token_hex(16)
    }
    return render(request, template_name, context)
