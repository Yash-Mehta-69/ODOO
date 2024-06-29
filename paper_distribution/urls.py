from django.urls import path
from . import views

app_name = "paper_distribution"
urlpatterns = [
    path('new_exam/', views.new_exam, name='new_exam')
    # path('exams', views.exams, name='exams')
]