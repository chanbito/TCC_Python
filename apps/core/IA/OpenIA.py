import os
import logging
import openai
from ..models import message
from ..form import messageForm
from decouple import config

openai.api_key = os.getenv(config("OPENAI_API_KEY"))

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

    #openai.api_key = os.getenv('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')
    openai.api_key = config("OPENAI_API_KEY")

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
    msg = ret['choices'][0]['text']

    data = {
        'mensagem' : msg,
        'token' : token,
        'is_human' : False 
    }
    form = messageForm(data)
    if form.is_valid():
        form.save()
        return data
    logging.error('form invalido')
    return data
