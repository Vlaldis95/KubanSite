# Generated by Django 4.2.1 on 2023-05-26 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging', models.CharField(blank=True, choices=[('Гофрокороб', 'Гофрокороб'), ('Телефизор', 'Телефизор')], max_length=10)),
                ('photo', models.ImageField(blank=True, upload_to='pages/', verbose_name='Изображение')),
                ('weight', models.CharField(max_length=10, verbose_name='Вес')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('expiration_date', models.CharField(max_length=15, verbose_name='Срок годности')),
                ('quantity_a', models.CharField(blank=True, max_length=15, null=True, verbose_name='Количество вложения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pages.category', verbose_name='Группа')),
            ],
        ),
    ]