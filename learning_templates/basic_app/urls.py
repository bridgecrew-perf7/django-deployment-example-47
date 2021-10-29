from django.urls import path       #Allows the path function to be used
from basic_app import views             #

#Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'), #Enter /relative to see this page
    path('other/', views.other, name = 'other')         #Enter /other to see this page
]
