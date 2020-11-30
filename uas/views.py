from django.shortcuts import render

def index(request):
	context={
		'judul' : 'Yoyo Case!'
	}
	return render(request, 'index.html', context)