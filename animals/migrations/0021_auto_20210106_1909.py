# Generated by Django 3.1.3 on 2021-01-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0020_auto_20210106_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciesgroup',
            name='related_species',
        ),
        migrations.AddField(
            model_name='species',
            name='species_group',
            field=models.ManyToManyField(null=True, to='animals.SpeciesGroup'),
        ),
        migrations.AddField(
            model_name='toy',
            name='suggested_species',
            field=models.ManyToManyField(blank=True, null=True, to='animals.SpeciesGroup'),
        ),
    ]
