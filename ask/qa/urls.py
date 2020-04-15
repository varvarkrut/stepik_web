from django.urls import path
from . import views
urlpatterns = [
path('', views.new),
path('popular/',views.popular),
path('quiestion/',views.question_one)
]
