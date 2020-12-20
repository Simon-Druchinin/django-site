from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField("Название", max_length=100)
    text = models.TextField("Текст")
    date = models.DateTimeField("Дата публикации", default=timezone.now)
    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", default='', upload_to='posts/')

    def __str__(self):
        return f'{self.title}'

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"