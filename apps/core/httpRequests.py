import sys,os
import logging
from urllib import request, response
from django.shortcuts import render
from urllib.request import HTTPHandler
from django.http import HttpResponse
from .Translators import GoogleTranslator

def do_GET(request, mensagem):

    msg = GoogleTranslator.translate_text(mensagem)
    print(msg)
    content = {
        '{"mensagem": "%s"}' % msg
    }
    content_type = 'application/json'
    status = 200
    return HttpResponse(content, content_type, status)