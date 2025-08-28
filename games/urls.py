from games import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from user import views as user_views

urlpatterns = [
    path('<int:id>/', views.gameDetails, name='game_detail'),
    path('', views.game_list, name='game_list'),
    path('buy_game/<int:id_game>', user_views.buyGame, name='buyGame'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)