from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Author(models.Model):
    # связь «один к одному» с встроенной моделью пользователей User.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'
        ordering = ['user']

        def __str__(self):
            return f'{self.user}'


class Post(models.Model):
    TYPES = [
        ('TANK', 'Танк'),
        ('HILL', 'Хилл'),
        ('DD', 'ДД'),
        ('MER', 'Торговец'),
        ('GILD', 'Гилдмастер'),
        ('KV', 'Квестгивер'),
        ('BS', 'Кузнец'),
        ('TAN', 'Кожевник'),
        ('ZE', 'Зельевар'),
        ('MI', 'Мастер заклинаний'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    postCategory = models.CharField(max_length=4, choices=TYPES, blank=False, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    content = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='image/', verbose_name='Изображение', blank=True)

    # Метод preview().
    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'id-{self.pk}: {self.title}'

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def priview(self):
        preview = f' {self.text[:124]}'
        return preview

    def get_absolute_url(self):
        return reverse('post')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ['id']





