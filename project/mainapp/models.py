from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50)
    desk = models.TextField(verbose_name='Описание')
