from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('add_show', views.add_show),
    path('shows/<int:shows_id>/', views.shows_page),
    path('shows/<int:shows_id>/edit', views.edit_page),
    path('shows/edit', views.edit),
    path('shows/<int:shows_id>/delete', views.destroy),
    path('shows/delete', views.delete),
]