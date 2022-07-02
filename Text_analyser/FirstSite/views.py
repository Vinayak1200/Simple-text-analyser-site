from django.shortcuts import render
from django.http import HttpResponse
import string
import hashlib

def intro(request):
    return render(request, 'intro_page.html')

def form(request):
    return render(request, 'form.html')

def last(request):
    return render(request, 'last_page.html')

def analyse(request):
    text = request.GET.get('text', 'default')
    
    removepunc = request.GET.get('removepunc', 'default')
    uppercase = request.GET.get('uppercase', 'default')
    lowercase = request.GET.get('lowercase', 'default')
    reverse = request.GET.get('reverse', 'default')
    hash = request.GET.get('hash', 'default')
    if removepunc=='on':
               punc_list = string.punctuation
               for val in text:
                   if val in punc_list:
                       text = text.replace(val, '')
               params = {'Analysed_text':text}

    if uppercase=='on':
        text = text.upper()
        params = {'Analysed_text':text}

    if lowercase=='on':
        text = text.lower()
        params = {'Analysed_text':text}

    if reverse=='on':
        text = text[::-1]
        params = {'Analysed_text':text}

        
    return render(request, 'analyse.html', params)


    