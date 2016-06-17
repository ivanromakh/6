from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from models import Character
# Create your views here.

def Selectcard(request):
    requestcontext = RequestContext(request)
    all_charaters = Character.objects.all()
    requestcontext['choosable_charater'] = all_charaters
    return render_to_response('choose_cards.html', requestcontext)

def Loadhomepage(request):
    requestcontext = RequestContext(request)
    return render_to_response('home_page.html', requestcontext)

def Start(request):
    post = get_object_or_404(Character, person=person)
    return render(request, 'home_page.html',{'post': post})