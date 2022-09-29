from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='photos/country', blank=True)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'countries'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Game(models.Model):
    STATUS = (
        ('ready-to-start', 'Ready to Start'),
        ('ongoing', 'Ongoing'),
        ('end', 'End')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Country, null=True, related_name='rel_category', on_delete=models.SET_NULL)
    team2 = models.ForeignKey(Country, null=True, related_name='rel_category_id', on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=STATUS)
    point1 = models.CharField(max_length=10, blank=True, null=True)
    point2 = models.CharField(max_length=10, blank=True, null=True)
    liveLink = models.CharField(max_length=150, blank=True, null=True)
    videoTitle = models.CharField(max_length=150, blank=True, null=True)
    video=models.FileField(upload_to="video/%y", blank=True, null=True)
    startTime = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'games'
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self): 
        return self.team1.name + " VS " + self.team2.name


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return str(self.game)



    