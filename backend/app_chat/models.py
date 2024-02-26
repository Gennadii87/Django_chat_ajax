from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Room(models.Model):
    objects = None
    name = models.CharField(max_length=256, unique=True, verbose_name='Комната')

    def __str__(self):
        return f'{self.name}'


class UserProfile(models.Model):
    objects = None
    name = models.CharField(max_length=256, unique=True)
    avatar = ThumbnailerImageField(resize_source={'size': (300, 300), 'crop': 'smart'},
                                   upload_to='djangochatserver',
                                   default='djangochatserver/default.jpg',
                                   verbose_name='Аватарка')
    avatar_small = ThumbnailerImageField(resize_source={'size': (30, 30), 'crop': 'smart'},
                                         upload_to='djangochatserver',
                                         default='djangochatserver/default_small.jpg',
                                         verbose_name='Аватарка маленькая')
    room = models.OneToOneField(Room, on_delete=models.SET_NULL, null=True, verbose_name='Комната')
    online = models.BooleanField(default=False, verbose_name='Онлайн')

    @staticmethod
    def user_list():
        users = UserProfile.objects.filter().order_by('name')
        return list(users)

    def __str__(self):
        return f'{self.name}: {self.room}'


class Message(models.Model):
    objects = None
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Автор')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')
    text = models.CharField(max_length=255, verbose_name='Текст')

    def __str__(self):
        return f'{self.author}: {self.room}'
