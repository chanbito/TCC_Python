from django.shortcuts import render
from .form import messageForm
from .models import message
import logging
import secrets
from .IA import OpenIA

# Create your views here.

def home(request,token):
    template_name ='core/home.html'
    # if not request['token']:
    #     token = secrets.token_hex(16)
    logging.warning(token)
    if token == "":
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

def translater(mensagem):
    template_name = 'core/home.html'
    context = {}
    logging.warning(mensagem)
    msg = GoogleTranslator.translate_text(mensagem)
    logging.warning(msg)
    
    #return msg
    return render('request', template_name, context)

    #   context = {}
    # logging.warning(mensagem)
    # msg = GoogleTranslator.translate_text(mensagem)
    # logging.warning(msg)
    # context['trad'] = msg
    # #return  context
    # return render(request,'NULL',context)
    # #return JSONEncoder(msg)