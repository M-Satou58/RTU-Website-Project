from django.shortcuts import render

# Create your views here.

def indexView(request):
	context = {}
	return render(request, 'index.html', context)

def seminarView(request):
	context = {}
	return render(request, 'seminar.html', context)

def recordOfPractieView(request):
	context = {}
	return render(request, 'record-of-practice.html', context)

def recordOfWebinarView(request):
	context = {}
	return render(request, 'record-of-webinar.html', context)

def openingView(request):
	context = {}
	return render(request, 'opening.html', context)

def shortClipsView(request):
	context = {}
	return render(request, 'short-clips.html', context)

def teaserView(request):
	context = {}
	return render(request, 'teaser.html', context)
