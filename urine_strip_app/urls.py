# urine_strip_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.process_urine_strip, name='upload'),
    # render the index.html template as the root URL
    path('', views.index, name='index'),
]
