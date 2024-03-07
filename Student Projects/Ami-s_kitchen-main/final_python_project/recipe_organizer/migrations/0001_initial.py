# Generated by Django 5.0.2 on 2024-02-18 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_text', models.TextField()),
                ('recipe_picture', models.ImageField(upload_to='recipe_FOLDER')),
            ],
        ),
    ]
