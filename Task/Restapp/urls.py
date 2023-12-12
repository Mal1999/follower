from django.contrib import admin
from django.urls import path, re_path
from . import views
app_name='Restapp'
urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('login/', views.login_view, name='login_view'),
    path(' logout/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('form/', views.form_page, name='form_page'),
    path('department/<str:department>/', views.department_view, name='department_view'),
    path('new_page/',views.new_page,name='new_page'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('form-confirm/<str:message>/', views.form_confirm, name='form_confirm'),


]

