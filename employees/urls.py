from django.urls import path
from . import views

urlpatterns = [
    path("", views.Employees.as_view()),
    path("<int:pk>/", views.EmployeeDetail.as_view()),

]
