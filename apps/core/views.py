from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import messageForm
import logging
import secrets
from .IA import OpenIA

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
        template_name ='core/home.html'
        
        msgForm = OpenIA.Interation(data['token'])
        logging.warning(msgForm)
        context = { 
            'token': data['token'],
            'mensagem': data
        }
        # return render(request, template_name, context)
        index_path = reverse('core:home')
        return HttpResponseRedirect(index_path)

def sending(request):
    template_name ='core/home.html'
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
            # return redirect('core:returning',data)
            return returning(data=data,request=request)

    return render(request, template_name, context)

def home(request):
    template_name ='core/home.html'
    context = {
        'token' : secrets.token_hex(16)
    }
    return render(request, template_name, context)

def render_message(request, data):
    #aqui teremos que renderizar a nova tela com a mensagem
    template_name ='core/home.html'
    context = {
        'token' : secrets.token_hex(16)
    }
    return render(request, template_name, context)
    