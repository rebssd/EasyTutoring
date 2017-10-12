from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def new(request):
	return render(request, 'disciplinas/new.html')
