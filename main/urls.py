from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('mode/<str:mode>/', views.mode_view, name='mode_view'),

    path('about/', views.about_view, name='about_view'),
    path('experience/', views.experience_view, name='experience_view'),
    path('projects/', views.projects_view, name='projects_view'),
    path('skills/', views.skills_view, name='skills_view'),
    path('contact/', views.contact_view, name='contact_view'),
    


]