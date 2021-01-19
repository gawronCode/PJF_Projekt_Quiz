from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('<int:quiz_id>/', views.solve, name='solve'),
    path('<int:quiz_id>/result/', views.result, name='result'),
    path('create/', views.create, name='create'),
]
