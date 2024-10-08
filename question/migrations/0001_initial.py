# Generated by Django 4.1.7 on 2023-05-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('question_text', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
