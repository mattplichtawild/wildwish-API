# Generated by Django 3.1.2 on 2021-08-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_id', models.CharField(blank=True, max_length=900, null=True)),
                ('caption', models.CharField(default='', max_length=2200)),
                ('user_tags', models.CharField(default='', max_length=2200)),
                ('hash_tags', models.JSONField(blank=True, null=True)),
                ('photos', models.ManyToManyField(to='images.Image')),
            ],
        ),
    ]