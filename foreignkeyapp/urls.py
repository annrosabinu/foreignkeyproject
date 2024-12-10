from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_student/', views.add_student, name='add_student'),
    path('show_details/', views.show_details, name='show_details'),
    path('editpage/<int:id>/', views.editpage, name='editpage'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
