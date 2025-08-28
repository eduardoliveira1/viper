from django.db import models
from games.models import Game 

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    biling = models.DecimalField(max_digits=100, decimal_places=2, default=0)

    def create_game(self, title, description, price, img):
        game = Game.objects.create(
            title=title,
            description=description,
            price=price,
            img=img,
            company=self
        )
        
    def delete_game(self, game_id):
        try:
            game = Game.objects.get(id=game_id, company=self)
            game.delete()
        except Game.DoesNotExist:
            print(f"Game not found!") 

    def edit_game(self, game_id, title=None, description=None, price=None, img=None):
        try:
            game = Game.objects.get(id=game_id, company=self)
            if title:
                game.title = title
            if description:
                game.description = description
            if price is not None:
                game.price = price
            if img:
                game.img = img
            game.save()
        except Game.DoesNotExist:
            print(f"Game not found!")