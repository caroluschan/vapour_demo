from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model): # Game
    user = models.ForeignKey(User, default=1) # 
    artist = models.CharField(max_length=250) # game developer
    album_title = models.CharField(max_length=500) # game name 
    genre = models.CharField(max_length=100)  # game genre
    album_logo = models.FileField() # game logo
    is_favorite = models.BooleanField(default=False) # purchased
    price = models.FloatField(default=0) # price
    release_date = models.CharField(max_length=30, default="01-04-2017") # release date
    support_platform = models.CharField(max_length=30, default='Windows') # support platform
    online_description = models.CharField(max_length=50, default='online desc')
    detailed_description = models.CharField(max_length=200, default='detailed desc')

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model): # tags
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # game reference
    song_title = models.CharField(max_length=250) # tage name
    audio_file = models.FileField(default='') # not needed
    is_favorite = models.BooleanField(default=False) # purchased

    def __str__(self):
        return self.song_title


class UserModel(models.Model):
    balance = models.FloatField(default=100) # bank balance
    rewards = models.FloatField(default=0) # rewards available
    purchase_1 = models.ForeignKey(Album, on_delete=models.CASCADE) # last purchase
    # purchase_2 = models.ForeignKey(Album, on_delete=models.CASCADE) # last last purchase
    # purchase_3 = models.ForeignKey(Album, on_delete=models.CASCADE) # last last last purchase

class Purchases(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE) # user reference
    game = models.ForeignKey(Album, on_delete=models.CASCADE) # game reference


#Triggers: 
# update purchases
# update balance and rewards