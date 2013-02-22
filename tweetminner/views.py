# Create your views here.
# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import MetaD_Tuits

def tweets(request):
	lista_tweets = MetaD_Tuits.objects.all()
	return render_to_response('tweets.html',{'lista_tweets':lista_tweets})

