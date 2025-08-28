from django.shortcuts import render, redirect
from .models import Game
from user.models import User

# Create your views here.
def game_list(request):
    games = Game.objects.all() 
    genres = Game.objects.values_list('genres', flat=True).distinct()

    user_id = request.session.get('user_id')
    
    user = None
    
    if user_id:  # se estiver logado, pega o usuário
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

    title = request.GET.get("title", "")
    genre = request.GET.get("genre", "")
    price = request.GET.get("price", "")

    # Aplicando filtros
    if title:
        games = games.filter(title__icontains=title)
    if genre:
        games = games.filter(genres__name__icontains=genre)
    if price:
        try:
            price_value = float(price)
            games = games.filter(price__lte=price_value)
        except ValueError:
            pass  # Ignora se não for número válido

    # Para preencher os selects no template
    genres = Game.objects.values_list('genres__name', flat=True).distinct().order_by('genres__name')

    context = {
        "request": request,  # necessário para manter os valores nos inputs do filtro
        'games': games,
        'genres': genres,
        'user': user,
        'filter_title': title,
        'filter_genre': genre,
        'filter_price': price,
    }

    if not user:
        return render(request, 'games/allGames.html', context)

    return render(request, 'games/allGames.html', context)

def gameDetails(request, id):
    game = Game.objects.get(id=id)
    user_id = request.session.get('user_id')
    
    user = User.objects.get(id=user_id) if user_id else None

    context = {
        'game': game,
        'user': user,
    }

    return render(request, 'games/details.html', context)
