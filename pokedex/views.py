from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, Trainer    
from .forms import PokemonForm
from django.shortcuts import redirect
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
    return HttpResponse(template.render({'form': form}, request))