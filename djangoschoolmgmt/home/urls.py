from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name='registration'),
    path('confirmation/', views.confirmation, name='confirmation'),  
    path('department/', views.department, name='department'),
    path('contact/', views.contact, name='contact'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
    path('biology/', views.biology_view, name='biology'),
    path('department/<int:pk>/business_administration/', views.business_administration_view, name='business_administration_detail'),
    path('department/<int:dept_id>/computer_science/', views.computer_science_view, name='computer_science_detail'),
    path('complaint_confirmation/', views.complaint_confirmation, name='complaint_confirmation'),

]
