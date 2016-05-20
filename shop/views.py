from django.shortcuts import render, render_to_response
from django.template import RequestContext
from datetime import datetime


def index(request):
    year = datetime.now().year
    return render_to_response('index.html', {'year': year}, context_instance=RequestContext(request))


def bootstrap_contents(request):
    return render_to_response('bootstrap.html', context_instance=RequestContext(request))
