from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='games/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='genresList')
    company = models.ForeignKey("company.Company", on_delete=models.CASCADE, related_name='company_of_game', null=True)

    def __str__(self):
        return self.title
