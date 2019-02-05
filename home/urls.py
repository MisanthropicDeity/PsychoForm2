from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('proceed1/', views.proceed1),
    path('proceed2/', views.proceed2),
    path('proceed3/', views.proceed3),
    path('proceed4/', views.proceed4),
    path('proceed5/', views.proceed5),
    path('proceed6/', views.proceed6),
    path('proceed7/', views.proceed7),
    path('proceed8/', views.proceed8),
    path('proceedf/', views.proceedf),
    path('fform/', views.fform),
    path('quest1/', views.question1),
    path('quest2/', views.question2),
    path('quest3/', views.question3),
    path('quest4/', views.question4),
    path('quest5/', views.question5),
    path('quest6/', views.question6),
    path('quest7/', views.question7),
    path('quest8/', views.question8),
    path('feedback/',views.feedbck)
]