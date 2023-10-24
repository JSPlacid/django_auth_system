from django.urls import path
from . import views
urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:quiz_id>/', views.quiz_question, name='quiz_question'),
    path('submit/', views.submit_quiz, name='submit_quiz'),

    path('answer/', views.answer_question, name='answer_question'),
]
