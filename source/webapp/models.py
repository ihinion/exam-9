from django.contrib.auth import get_user_model
from django.db import models


class Photo(models.Model):
    picture = models.ImageField(upload_to='pics', verbose_name='Photo')
    desc = models.CharField(max_length=200, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               related_name='photos', verbose_name='Author')


class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), related_name='photo_favorites', verbose_name='User',
                             on_delete=models.CASCADE)
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE, related_name='favorites',
                                verbose_name='Photo')

    # def __str__(self):
    #     return f'{self.author.username} - {self.photo.desc}'

