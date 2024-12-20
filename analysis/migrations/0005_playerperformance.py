# Generated by Django 5.1.1 on 2024-10-13 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_alter_matchinfo_season_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_number', models.IntegerField(blank=True, null=True)),
                ('jersey_number', models.IntegerField(blank=True, null=True)),
                ('position', models.CharField(blank=True, max_length=10, null=True)),
                ('substitute', models.CharField(blank=True, max_length=10, null=True)),
                ('player_name', models.CharField(blank=True, max_length=255, null=True)),
                ('player_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('player_short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('player_position', models.CharField(blank=True, max_length=10, null=True)),
                ('player_jersey_number', models.IntegerField(blank=True, null=True)),
                ('player_height', models.IntegerField(blank=True, null=True)),
                ('player_user_count', models.IntegerField(blank=True, null=True)),
                ('player_id', models.IntegerField(blank=True, null=True)),
                ('country_alpha2', models.CharField(blank=True, max_length=5, null=True)),
                ('country_alpha3', models.CharField(blank=True, max_length=5, null=True)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('country_slug', models.CharField(blank=True, max_length=255, null=True)),
                ('market_value_currency', models.CharField(blank=True, max_length=5, null=True)),
                ('date_of_birth_timestamp', models.BigIntegerField(blank=True, null=True)),
                ('ATT_goals', models.IntegerField(blank=True, null=True)),
                ('ATT_goal_assist', models.IntegerField(blank=True, null=True)),
                ('ATT_shot_off_target', models.IntegerField(blank=True, null=True)),
                ('ATT_hit_woodwork', models.IntegerField(blank=True, null=True)),
                ('ATT_big_chance_created', models.IntegerField(blank=True, null=True)),
                ('ATT_big_chance_missed', models.IntegerField(blank=True, null=True)),
                ('ATT_on_target_scoring_attempt', models.IntegerField(blank=True, null=True)),
                ('ATT_expected_goals', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ATT_expected_assists', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ATT_penalty_won', models.IntegerField(blank=True, null=True)),
                ('ATT_penalty_miss', models.IntegerField(blank=True, null=True)),
                ('PAS_total_passes', models.IntegerField(blank=True, null=True)),
                ('PAS_accurate_passes', models.IntegerField(blank=True, null=True)),
                ('PAS_key_passes', models.IntegerField(blank=True, null=True)),
                ('PAS_crosses', models.IntegerField(blank=True, null=True)),
                ('PAS_accurate_crosses', models.IntegerField(blank=True, null=True)),
                ('PAS_long_balls', models.IntegerField(blank=True, null=True)),
                ('PAS_accurate_long_balls', models.IntegerField(blank=True, null=True)),
                ('MUC_duel_won', models.IntegerField(blank=True, null=True)),
                ('MUC_aerial_duel_won', models.IntegerField(blank=True, null=True)),
                ('MUC_duel_lost', models.IntegerField(blank=True, null=True)),
                ('MUC_aerial_lost', models.IntegerField(blank=True, null=True)),
                ('MUC_won_contest', models.IntegerField(blank=True, null=True)),
                ('MUC_challenge_lost', models.IntegerField(blank=True, null=True)),
                ('MUC_total_contest', models.IntegerField(blank=True, null=True)),
                ('MUC_possession_lost', models.IntegerField(blank=True, null=True)),
                ('MUC_fouls_committed', models.IntegerField(blank=True, null=True)),
                ('MUC_fouls_suffered', models.IntegerField(blank=True, null=True)),
                ('MUC_offsides', models.IntegerField(blank=True, null=True)),
                ('MUC_dispossessed', models.IntegerField(blank=True, null=True)),
                ('MUC_error_lead_to_a_shot', models.IntegerField(blank=True, null=True)),
                ('MUC_error_lead_to_a_goal', models.IntegerField(blank=True, null=True)),
                ('DEF_clearances', models.IntegerField(blank=True, null=True)),
                ('DEF_blocked_scoring_attempt', models.IntegerField(blank=True, null=True)),
                ('DEF_tackles', models.IntegerField(blank=True, null=True)),
                ('DEF_interceptions', models.IntegerField(blank=True, null=True)),
                ('DEF_last_man_tackle', models.IntegerField(blank=True, null=True)),
                ('DEF_penalty_conceded', models.IntegerField(blank=True, null=True)),
                ('DEF_own_goals', models.IntegerField(blank=True, null=True)),
                ('DEF_clearance_off_line', models.IntegerField(blank=True, null=True)),
                ('DEF_outfielder_block', models.IntegerField(blank=True, null=True)),
                ('KAL_good_high_claim', models.IntegerField(blank=True, null=True)),
                ('KAL_saved_shots_from_inside_the_box', models.IntegerField(blank=True, null=True)),
                ('KAL_saves', models.IntegerField(blank=True, null=True)),
                ('KAL_punches', models.IntegerField(blank=True, null=True)),
                ('KAL_total_keeper_sweeper', models.IntegerField(blank=True, null=True)),
                ('KAL_accurate_keeper_sweeper', models.IntegerField(blank=True, null=True)),
                ('KAL_goals_prevented', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('KAL_penalty_save', models.IntegerField(blank=True, null=True)),
                ('KAL_penalty_shootout_save', models.IntegerField(blank=True, null=True)),
                ('KAL_penalty_shootout_goal', models.IntegerField(blank=True, null=True)),
                ('KAL_penalty_shootout_miss', models.IntegerField(blank=True, null=True)),
                ('match_id', models.IntegerField(blank=True, null=True)),
                ('team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('team_id', models.IntegerField(blank=True, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
                ('minutes_played', models.IntegerField(blank=True, null=True)),
                ('touches', models.IntegerField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('rating_original', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('rating_alternative', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('player_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('player_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_translation_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('short_name_translation_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('captain', models.BooleanField(default=False)),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('match_id', 'player_id'), name='unique_match_player')],
            },
        ),
    ]
