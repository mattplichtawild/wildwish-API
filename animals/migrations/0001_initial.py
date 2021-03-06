# Generated by Django 3.1.2 on 2021-07-04 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=24)),
                ('date_of_birth', models.DateField(blank=True, help_text='YYYY-MM-DD', null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avatar_img', to='images.image')),
                ('images', models.ManyToManyField(to='images.Image')),
            ],
            options={
                'db_table': 'animals',
            },
        ),
        migrations.CreateModel(
            name='SpeciesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=72)),
            ],
            options={
                'verbose_name': 'Species Group',
            },
        ),
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ship_cost', models.DecimalField(blank=True, decimal_places=2, help_text='Leave blank if unknown.', max_digits=6, null=True)),
                ('brand', models.CharField(blank=True, max_length=180, null=True)),
                ('url', models.URLField(max_length=1200, null=True)),
                ('images', models.ManyToManyField(to='images.Image')),
                ('suggested_species', models.ManyToManyField(blank=True, to='animals.SpeciesGroup')),
            ],
            options={
                'db_table': 'toys',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=72)),
                ('website', models.CharField(max_length=72)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=False)),
                ('fund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('images', models.ManyToManyField(blank=True, to='images.Image')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.toy')),
            ],
            options={
                'verbose_name_plural': 'Wishes',
                'db_table': 'wishes',
            },
        ),
        migrations.AddField(
            model_name='toy',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.vendor'),
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=72)),
                ('genus', models.CharField(blank=True, max_length=72, null=True)),
                ('species', models.CharField(blank=True, max_length=72, null=True)),
                ('sub_species', models.CharField(blank=True, max_length=72, null=True)),
                ('species_group', models.ManyToManyField(blank=True, to='animals.SpeciesGroup')),
            ],
            options={
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='animals.species'),
        ),
    ]
