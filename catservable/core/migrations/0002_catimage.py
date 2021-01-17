# Generated by Django 3.1.5 on 2021-01-13 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0002_auto_20210112_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatImage',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.catbreed')),
            ],
        ),
    ]