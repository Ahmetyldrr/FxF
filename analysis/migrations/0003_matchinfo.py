# Generated by Django 5.1.1 on 2024-10-11 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_matchstats_delete_fixturedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchInfo',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tournament_category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('tournament_category_id', models.IntegerField(blank=True, null=True)),
                ('tournament_category_country_code', models.CharField(blank=True, max_length=3, null=True)),
                ('unique_tournament_id', models.IntegerField(blank=True, null=True)),
                ('tournament_is_group', models.BooleanField(blank=True, null=True)),
                ('tournament_id', models.IntegerField(blank=True, null=True)),
                ('season_name', models.CharField(blank=True, max_length=255, null=True)),
                ('season_year', models.IntegerField(blank=True, null=True)),
                ('season_id', models.IntegerField(blank=True, null=True)),
                ('round_info', models.CharField(blank=True, max_length=255, null=True)),
                ('custom_id', models.CharField(blank=True, max_length=255, null=True)),
                ('home_team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('home_team_user_count', models.IntegerField(blank=True, null=True)),
                ('home_team_manager_name', models.CharField(blank=True, max_length=255, null=True)),
                ('home_team_id', models.IntegerField(blank=True, null=True)),
                ('away_team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('away_team_user_count', models.IntegerField(blank=True, null=True)),
                ('away_team_manager_name', models.CharField(blank=True, max_length=255, null=True)),
                ('away_team_id', models.IntegerField(blank=True, null=True)),
                ('home_score_period1', models.IntegerField(blank=True, null=True)),
                ('home_score_period2', models.IntegerField(blank=True, null=True)),
                ('home_score_normaltime', models.IntegerField(blank=True, null=True)),
                ('away_score_period1', models.IntegerField(blank=True, null=True)),
                ('away_score_period2', models.IntegerField(blank=True, null=True)),
                ('away_score_normaltime', models.IntegerField(blank=True, null=True)),
                ('has_global_highlights', models.BooleanField(blank=True, null=True)),
                ('has_event_player_statistics', models.BooleanField(blank=True, null=True)),
                ('has_event_player_heat_map', models.BooleanField(blank=True, null=True)),
                ('start_timestamp', models.DateTimeField(blank=True, null=True)),
                ('event_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('round_info_name', models.CharField(blank=True, max_length=255, null=True)),
                ('round_info_slug', models.SlugField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
