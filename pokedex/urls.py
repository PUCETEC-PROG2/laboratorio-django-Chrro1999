from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),     
    path("trainer/<int:id>/", views.trainer, name="trainer"),    
    path("pokedex/", views.pokedex, name="pokedex"),              
    path("trainers/", views.trainers, name="trainers"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("pokemon/<int:id>/edit/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/<int:id>/delete/", views.delete_pokemon, name="delete_pokemon"),
    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]