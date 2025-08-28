from django.contrib import admin
from .models import Game, Genre  # substitua 'Game' pelo nome do seu modelo

admin.site.register(Genre)
admin.site.register(Game)