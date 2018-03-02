from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
	if request.session.get('words') == None:
		request.session['words'] = []

	return render(request, 'session_words_app/index.html')

def process(request):
	print "success!"

	word = request.POST['word']
	color = request.POST['color']
	if 'big_font' in request.POST:
		font = "big"
	else:
		font = "normal"
	added = datetime.strftime(datetime.now(), "%H:%M:%S %p, %B %d, %Y")

	request.session['words'].append({'word': word, 'color': color, 'font': font, 'added': added})
	request.session.modified = True
	return redirect('/')

def clear(request):
	request.session.clear()
	return redirect('/')
