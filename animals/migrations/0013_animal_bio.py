# Generated by Django 3.1.3 on 2021-01-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0012_remove_animal_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='bio',
            field=models.TextField(help_text='Max 180 characters', null=True),
        ),
    ]
