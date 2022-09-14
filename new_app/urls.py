from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.redirect),
    path('redirect/', views.redirect),
    path('about/', views.about, name='about'),
    path("book_details/<int:pk>/", views.book_details, name="book_details"),
    path("book_list/", views.book_list, name="book_list")

]
