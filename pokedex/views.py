from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer    
from .forms import PokemonForm
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse

def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()  
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'trainers': trainers}, request))

def pokemon(request, id:int):  
    pokemon = Pokemon.objects.get(id=id)
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon
    }
    return HttpResponse(template.render(context, request))

def trainer(request, id:int):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {
        'trainer': trainer
    }
    return HttpResponse(template.render(context, request))

# ✅ AGREGAR esta vista que falta para la ruta pokedex/
def pokedex(request):
    pokemons = Pokemon.objects.all()
    template = loader.get_template('pokedex.html')  
    context = {
        'pokemons': pokemons
    }
    return HttpResponse(template.render(context, request))


def trainers(request):
    trainers_list = Trainer.objects.all()
    template = loader.get_template('trainers.html')
    context = {
        'trainers': trainers_list
    }
    return HttpResponse(template.render(context, request))


def add_pokemon(request):
    """View to add a new Pokemon via form (handles image upload)."""
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            pokemon = form.save()
            # redirect to the pokemon detail page if available
            try:
                return redirect(reverse('pokemon', args=[pokemon.id]))
            except Exception:
                return redirect('pokedex')
    else:
        form = PokemonForm()

    template = loader.get_template('pokemon_form.html')
    return HttpResponse(template.render({'form': form, 'title': 'Agregar Pokémon', 'submit_label': 'Agregar'}, request))


@login_required
def edit_pokemon(request, id:int):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            pokemon = form.save()
            logout(request)  # Logout after successful edit
            try:
                return redirect(reverse('pokemon', args=[pokemon.id]))
            except Exception:
                return redirect('pokedex')
    else:
        form = PokemonForm(instance=pokemon)

    template = loader.get_template('pokemon_form.html')
    return HttpResponse(template.render({'form': form, 'title': 'Editar Pokémon', 'submit_label': 'Guardar cambios'}, request))


@login_required
def delete_pokemon(request, id:int):
    pokemon = get_object_or_404(Pokemon, id=id)
    if request.method == 'POST':
        pokemon.delete()
        logout(request)  # Logout after successful delete
        return redirect('pokedex')

    # If GET, show a simple confirmation page using the display template
    template = loader.get_template('display_pokemon.html')
    context = {
        'pokemon': pokemon,
        'confirm_delete': True,
        'delete_url': reverse('delete_pokemon', args=[pokemon.id]),
    }
    return HttpResponse(template.render(context, request))