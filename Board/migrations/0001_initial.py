# Generated by Django 4.2.8 on 2024-05-01 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'автор',
                'verbose_name_plural': 'авторы',
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('postCategory', models.CharField(choices=[('TANK', 'Танк'), ('HILL', 'Хилл'), ('DD', 'ДД'), ('MER', 'Торговец'), ('GILD', 'Гилдмастер'), ('KV', 'Квестгивер'), ('BS', 'Кузнец'), ('TAN', 'Кожевник'), ('ZE', 'Зельевар'), ('MI', 'Мастер заклинаний')], max_length=4, verbose_name='Категория')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('content', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='image/', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.author', verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('commentPost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.post')),
                ('commentUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'ordering': ['id'],
            },
        ),
    ]