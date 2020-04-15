from django.urls import path
from . import views
urlpatterns = [
path('', views.new, name='index'),
path('popular/',views.popular),
path('quiestion/',views.question)
]
