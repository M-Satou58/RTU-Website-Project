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

def financeRadioView(request):
	context = {}
	return render(request, 'finance-radio.html', context)

def othersForDocumentationView(request):
	context = {}
	return render(request, 'others-for-documentation.html', context)

def photoOpWithMsRonaView(request):
	context = {}
	return render(request, 'photo-op-with-ms-rona.html', context)

def photoOpWithParticipantsView(request):
	context = {}
	return render(request, 'photo-op-with-participants.html', context)



def presentationSlidesView(request):
	context = {}
	return render(request, 'presentation-slides.html', context)



def speakerView(request):
	context = {}
	return render(request, 'speaker.html', context)

def aboutTheSeminarView(request):
	context = {}
	return render(request, 'about-the-seminar.html', context)

def narrativeReportView(request):
	context = {}
	return render(request, 'narrative-report.html', context)