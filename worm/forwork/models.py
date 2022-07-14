from django.db import models


# Create your models here.

class Role(models.Model):
    kat = (
        ('специалист', 'специалист'),
        ('служащий', 'служащий'),
        ('рабочий', 'рабочий'),
    )
    Name = models.CharField('Name', max_length=40, default="")
    Kategor = models.CharField('Kategory', max_length=20, choices=kat)

    #При изменении отправляет на страничку ролей
    def get_absolute_url(self):
        return f'/Roles'

class Staf(models.Model):
    FIO = models.CharField('FIO', max_length=60)
    Gender = models.CharField('Gender', max_length=1)
    Age = models.IntegerField('Age')
    Post = models.ForeignKey( Role, on_delete=models.SET_DEFAULT, default='1')

    def __str__(self):
        return self.FIO

    # При изменении отправляет на личную карточку
    def get_absolute_url(self):
        return f'/{self.id}'