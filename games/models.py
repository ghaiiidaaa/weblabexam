from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)  # Developer's name cannot be null

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)  # Title of the game
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)  # ForeignKey to Developer

    def __str__(self):
        return self.title
