# Generated by Django 3.2 on 2021-11-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stage4', '0002_auto_20211111_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paint', models.IntegerField()),
                ('beauty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hole', models.IntegerField()),
                ('score', models.IntegerField()),
            ],
        ),
    ]