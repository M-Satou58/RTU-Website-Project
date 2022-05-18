from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexView, name='index'),
    path('seminar/', views.seminarView, name='seminar'),
    path('record-of-practice/', views.recordOfPractieView, name='record-of-practice'),
    path('record-of-webinar/', views.recordOfWebinarView, name='record-of-webinar'),
    path('opening/', views.openingView, name='opening'),
    path('short-clips/', views.shortClipsView, name='short-clips'),
    path('teaser/', views.teaserView, name='teaser'),
    path('finance-radio/', views.financeRadioView, name='finance-radio'),
    path('others-for-documentation/', views.othersForDocumentationView, name='others-for-documentation'),
    path('photo-op-with-ms-rona/', views.photoOpWithMsRonaView, name='photo-op-with-ms-rona'),
    path('photo-op-with-participants/', views.photoOpWithParticipantsView, name='photo-op-with-participants'),
    path('presentation-slides/', views.presentationSlidesView, name='presentation-slides'),
    path('speaker/', views.speakerView, name='speaker'),
    path('about-the-seminar/', views.aboutTheSeminarView, name='about-the-seminar'),
    path('narrative-report/', views.narrativeReportView, name='narrative-report'),
]
