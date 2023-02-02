from django.urls import path, include
from . import views

urlpatterns = [
    path('tests/add/questions',views.add_questions, name='add_questions' ),
    path('create',views.create_tests, name='create_tests' ),
    path('', views.show_tests, name='show_tests'),
    path('tests/<int:tests_pk>', views.tests_detail, name='tests_detail'),
    path('tests/delete/questions/<int:question_pk>', views.delete_question, name='delete_question'),
    path('tests/edit/questions/<int:question_pk>', views.edit_question, name='edit_question'),
    path('testing/<int:test_pk>', views.testing, name='testing'),
    path('testing/checking/<int:test_pk>', views.check, name='check'),
    path('tests/delete/test/<int:test_pk>', views.delete_test, name='delete_test'),



    
]