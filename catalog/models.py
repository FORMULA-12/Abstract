from django.db import models
import uuid
import os


def path_and_rename(instance, filename):
    upload_to = 'books/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid.uuid4()), ext)

    return os.path.join(upload_to, filename)


class Tags(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']

    title = models.CharField(max_length=30)


class Books(models.Model):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    CATEGORY = (('0', 'Художественная литература'), ('1', 'Научно-популярная литература'), ('2', 'Справочная литература'), ('3', 'Документальная проза'), ('4', 'Учебная литература'))
    LANGUAGES = (('RU', 'Русский'), ('UK', 'Украинский'), ('EN', 'Английский'), ('DE', 'Немецкий'), ('FR', 'Французский'), ('ES', 'Испанский'))

    title = models.CharField(null=False, max_length=100, verbose_name='Название')
    description = models.CharField(null=False, blank=True, max_length=1000, verbose_name='Описание')
    author = models.CharField(null=False, max_length=100, verbose_name='Автор')
    picture = models.ImageField(upload_to=path_and_rename, blank=True)
    category = models.CharField(null=False, max_length=1, choices=CATEGORY, default='0', verbose_name='Категория')
    language = models.CharField(null=False, max_length=2, choices=LANGUAGES, default='RU', verbose_name='Язык')
    date = models.CharField(null=False, blank=True, max_length=20, verbose_name='Дата')
    tags = models.ManyToManyField(Tags, verbose_name='Теги')
    presence = models.BooleanField(null=False, default=True, verbose_name='В наличии')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    published = models.DateTimeField(null=False, auto_now_add=True)
