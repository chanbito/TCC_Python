from fnmatch import translate
from decouple import config
from googletrans import Translator

def translate_text(text="Hello, world!"):
    
    trad = Translator()
    msg = trad.translate(text,dest='pt').text
    print(msg)
    #ja ta retornando mensagem
    return msg
