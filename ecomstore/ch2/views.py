from ch2.models import *
from django.http import HttpResponse
from django.template import * # Context
from django.template.loader import render_to_string


# def catalog(request): 

#     site_name = "Modern Musician" 

#     response_html = u"<html><body>Welcome to %s.</body></html>" % site_name 

#     return HttpResponse(response_html) 

def catalog(request): 



    my_context = Context({ 'site_name': 'Modern Musician' }) 



    # response_html = return_to_string('sample.html', my_context) 
    response_html = render_to_string('sample.html', my_context) 


    return HttpResponse(response_html)