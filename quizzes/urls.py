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
    path('add_question/<int:quiz_id>/', views.add_question, name='add_question'),
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('add_answer/<int:question_id>/', views.add_answer, name='add_answer'),
    path('delete_answer/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('update_answer/<int:answer_id>/', views.update_answer, name='update_answer'),

]
