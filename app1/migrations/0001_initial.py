# Generated by Django 5.1.4 on 2025-03-10 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('t_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloud', models.IntegerField(max_length=100)),
                ('t_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('url', models.URLField(default='http://byekvk.com')),
                ('t_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.topic')),
            ],
        ),
    ]
