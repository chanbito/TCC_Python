from ctypes import sizeof
import os
import logging
import openai
from ..models import message
from ..form import messageForm
from decouple import config

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def Interation(token):
    logging.warning('testaremos')
    #pegar objetos do banco e filrar pelo token q ta vindo
    messageobj = message.objects.filter(token=token).values('mensagem','is_human')

    prompt = ' '
    for var in messageobj:
        if var['is_human']:
            prompt += restart_sequence + var['mensagem']
        else:
            prompt += start_sequence + var['mensagem']

    logging.warning(prompt)

    openai.api_key = config("OPENAI_API_KEY")

    logging.error('promp' + prompt)


    ret = openai.Completion.create(
        engine="text-davinci-002",
        prompt= prompt,
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.0,
        stop=[" Human:", " AI:"]
    )

    logging.error(ret)

    msg = ret['choices'][0]['text'].split(':')
    logging.error(msg)
    data = {
        'mensagem' : msg[len(msg)-1],
        'token' : token,
        'is_human' : False 
    }
    form = messageForm(data)
    if form.is_valid():
        form.save()
        return data
    logging.error('form invalido')
    return data
