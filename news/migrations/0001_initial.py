# Generated by Django 4.1.7 on 2023-05-20 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='news-images/')),
                ('content', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now_add=True)),
                ('authors', models.ManyToManyField(to='news.author')),
            ],
        ),
    ]
