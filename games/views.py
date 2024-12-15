# views.py
from django.shortcuts import render

def game_list(request):
    # A simple list of games and their developers
    games = [
        {'title': 'The Legend of Zelda: Breath of the Wild', 'developer': 'Nintendo'},
        {'title': 'Cyberpunk 2077', 'developer': 'CD Projekt Red'},
        {'title': 'Halo Infinite', 'developer': '343 Industries'},
        {'title': 'The Witcher 3: Wild Hunt', 'developer': 'CD Projekt Red'},
        {'title': 'Minecraft', 'developer': 'Mojang Studios'}
    ]
    return render(request, 'game_list.html', {'games': games})

# games/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Rendering the home template
