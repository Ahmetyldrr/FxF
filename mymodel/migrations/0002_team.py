# Generated by Django 5.1.1 on 2024-10-20 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('team_name', models.CharField(max_length=255)),
                ('team_slug', models.SlugField(max_length=255)),
                ('team_shortName', models.CharField(max_length=100)),
                ('team_nameCode', models.CharField(max_length=10)),
                ('team_national', models.BooleanField(default=False)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymodel.season')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymodel.tournament')),
            ],
        ),
    ]
