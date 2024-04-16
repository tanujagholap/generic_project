from django.urls import path
from .views import Add_student, List_student, Detail_student, Update_student, Delete_student

urlpatterns = [
    path('', Add_student.as_view()),
    path('list/', List_student.as_view()),
    path('detail/<pk>/', Detail_student.as_view()),
    path('update/<pk>/', Update_student.as_view()),
    path('delete/<pk>/', Delete_student.as_view()),
]