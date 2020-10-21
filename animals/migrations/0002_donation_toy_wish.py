# Generated by Django 3.1.2 on 2020-10-21 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='animals.toy')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.user')),
                ('wish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.wish')),
            ],
        ),
    ]