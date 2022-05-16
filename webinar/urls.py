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
]
