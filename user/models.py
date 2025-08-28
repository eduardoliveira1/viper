from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12)
    profile_picture = models.ImageField(upload_to='user/', default='user/user.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    purchased_games = models.ManyToManyField("games.Game", blank=True)
    online = models.BooleanField(default=False)

    def buyGame(self, game):
        self.purchased_games.add(game)
        if game.company:
            print(game.company.biling)
            game.company.biling += game.price
            game.company.save()
            print(game.company.biling)
        self.save()

    def delete_account(self):
        self.delete()
        
    def logout(self):
        self.online = False
        self.save()

def find_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    
def create_user(username, first_name, last_name, email, password, profile_picture=None, online=True):
    if profile_picture is None:
        profile_picture = 'user/user.png'
    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        profile_picture=profile_picture,
        online=online
    )
    return user
