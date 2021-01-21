from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/', views.select, name='select'),
    path('solve/<int:quiz_id>/', views.solve, name='solve'),
    path('result/<int:quiz_id>/', views.result, name='result'),
    path('manage/', views.manage, name='manage'),
    path('create/', views.create, name='create'),
    path('delete/<int:quiz_id>/', views.delete, name='delete'),
    path('edit/<int:quiz_id>/', views.edit, name='edit'),

]
