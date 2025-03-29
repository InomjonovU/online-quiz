from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_quiz, name='add'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/add_question/', views.add_question, name='add_question'),
    path('quiz/<int:quiz_id>/edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('quiz/<int:quiz_id>/delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('quiz/<int:quiz_id>/delete/', views.delete_quiz, name='delete_quiz'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact/', views.contacts, name='contact'),
]