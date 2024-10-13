
from django.utils import timezone
from django.db import models


class MatchStats(models.Model):
    """
    Maç istatistiklerini saklamak için kullanılan model.
    """

    # 'id' alanı manuel olarak girilecek ve benzersiz (unique) olacak
    id = models.IntegerField(primary_key=True, verbose_name="Maç ID")

    # Tarih alanı manuel olarak girilecek ve normal bir DateField olacak
    tarih = models.DateField(verbose_name="Tarih")

    # JSONField olarak tanımlanan 'stats' alanı
    stats = models.JSONField(verbose_name="İstatistikler", default=dict, blank=True)

    # Otomatik olarak güncellenen tarih bilgisi (model her güncellendiğinde değişir)
    update_date = models.DateTimeField(auto_now=True, verbose_name="Güncelleme Tarihi")

    def __str__(self):
        return f"Maç ID: {self.id} - Tarih: {self.tarih}"










from django.db import models

class MatchInfo(models.Model):
    match_id = models.IntegerField(primary_key=True)  # match_id alanı birincil anahtar olarak tanımlandı, bu yüzden null ve blank eklenmedi.
    tournament_name = models.CharField(max_length=255, null=True, blank=True)
    tournament_category_name = models.CharField(max_length=255, null=True, blank=True)
    tournament_category_id = models.IntegerField(null=True, blank=True)
    tournament_category_country_code = models.CharField(max_length=3, null=True, blank=True)
    unique_tournament_id = models.IntegerField(null=True, blank=True)
    tournament_is_group = models.BooleanField(null=True, blank=True)
    tournament_id = models.IntegerField(null=True, blank=True)
    season_name = models.CharField(max_length=255, null=True, blank=True)
    season_year = models.CharField(max_length=255, null=True, blank=True)
    season_id = models.IntegerField(null=True, blank=True)
    round_info = models.CharField(max_length=255, null=True, blank=True)
    custom_id = models.CharField(max_length=255, null=True, blank=True)
    home_team_name = models.CharField(max_length=255, null=True, blank=True)
    home_team_user_count = models.IntegerField(null=True, blank=True)
    home_team_manager_name = models.CharField(max_length=255, null=True, blank=True)
    home_team_id = models.IntegerField(null=True, blank=True)
    away_team_name = models.CharField(max_length=255, null=True, blank=True)
    away_team_user_count = models.IntegerField(null=True, blank=True)
    away_team_manager_name = models.CharField(max_length=255, null=True, blank=True)
    away_team_id = models.IntegerField(null=True, blank=True)
    home_score_period1 = models.IntegerField(null=True, blank=True)
    home_score_period2 = models.IntegerField(null=True, blank=True)
    home_score_normaltime = models.IntegerField(null=True, blank=True)
    away_score_period1 = models.IntegerField(null=True, blank=True)
    away_score_period2 = models.IntegerField(null=True, blank=True)
    away_score_normaltime = models.IntegerField(null=True, blank=True)
    has_global_highlights = models.BooleanField(null=True, blank=True)
    has_event_player_statistics = models.BooleanField(null=True, blank=True)
    has_event_player_heat_map = models.BooleanField(null=True, blank=True)
    start_timestamp = models.DateTimeField(null=True, blank=True)
    event_slug = models.SlugField(max_length=255, null=True, blank=True)
    round_info_name = models.CharField(max_length=255, null=True, blank=True)
    round_info_slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.match_id} - {self.tournament_name}"








from django.db import models

class PlayerPerformance(models.Model):
    # Basic Player Information
    shirt_number = models.IntegerField(blank=True, null=True)
    jersey_number = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    substitute = models.CharField(max_length=10, blank=True, null=True)
    player_name = models.CharField(max_length=255, blank=True, null=True)
    player_slug = models.CharField(max_length=255, blank=True, null=True)
    player_short_name = models.CharField(max_length=255, blank=True, null=True)
    player_position = models.CharField(max_length=10, blank=True, null=True)
    player_jersey_number = models.IntegerField(blank=True, null=True)
    player_height = models.IntegerField(blank=True, null=True)
    player_user_count = models.IntegerField(blank=True, null=True)
    player_id = models.IntegerField(blank=True, null=True)

    # Player Country Information
    country_alpha2 = models.CharField(max_length=5, blank=True, null=True)
    country_alpha3 = models.CharField(max_length=5, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    country_slug = models.CharField(max_length=255, blank=True, null=True)
    market_value_currency = models.CharField(max_length=5, blank=True, null=True)
    date_of_birth_timestamp = models.BigIntegerField(blank=True, null=True)

    # Attack Statistics (ATT)
    ATT_goals = models.IntegerField(blank=True, null=True)
    ATT_goal_assist = models.IntegerField(blank=True, null=True)
    ATT_shot_off_target = models.IntegerField(blank=True, null=True)
    ATT_hit_woodwork = models.IntegerField(blank=True, null=True)
    ATT_big_chance_created = models.IntegerField(blank=True, null=True)
    ATT_big_chance_missed = models.IntegerField(blank=True, null=True)
    ATT_on_target_scoring_attempt = models.IntegerField(blank=True, null=True)
    ATT_expected_goals = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ATT_expected_assists = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ATT_penalty_won = models.IntegerField(blank=True, null=True)
    ATT_penalty_miss = models.IntegerField(blank=True, null=True)

    # Passing Statistics (PAS)
    PAS_total_passes = models.IntegerField(blank=True, null=True)
    PAS_accurate_passes = models.IntegerField(blank=True, null=True)
    PAS_key_passes = models.IntegerField(blank=True, null=True)
    PAS_crosses = models.IntegerField(blank=True, null=True)
    PAS_accurate_crosses = models.IntegerField(blank=True, null=True)
    PAS_long_balls = models.IntegerField(blank=True, null=True)
    PAS_accurate_long_balls = models.IntegerField(blank=True, null=True)

    # Duels and Fouls (MUC)
    MUC_duel_won = models.IntegerField(blank=True, null=True)
    MUC_aerial_duel_won = models.IntegerField(blank=True, null=True)
    MUC_duel_lost = models.IntegerField(blank=True, null=True)
    MUC_aerial_lost = models.IntegerField(blank=True, null=True)
    MUC_won_contest = models.IntegerField(blank=True, null=True)
    MUC_challenge_lost = models.IntegerField(blank=True, null=True)
    MUC_total_contest = models.IntegerField(blank=True, null=True)
    MUC_possession_lost = models.IntegerField(blank=True, null=True)
    MUC_fouls_committed = models.IntegerField(blank=True, null=True)
    MUC_fouls_suffered = models.IntegerField(blank=True, null=True)
    MUC_offsides = models.IntegerField(blank=True, null=True)
    MUC_dispossessed = models.IntegerField(blank=True, null=True)
    MUC_error_lead_to_a_shot = models.IntegerField(blank=True, null=True)
    MUC_error_lead_to_a_goal = models.IntegerField(blank=True, null=True)

    # Defensive Actions (DEF)
    DEF_clearances = models.IntegerField(blank=True, null=True)
    DEF_blocked_scoring_attempt = models.IntegerField(blank=True, null=True)
    DEF_tackles = models.IntegerField(blank=True, null=True)
    DEF_interceptions = models.IntegerField(blank=True, null=True)
    DEF_last_man_tackle = models.IntegerField(blank=True, null=True)
    DEF_penalty_conceded = models.IntegerField(blank=True, null=True)
    DEF_own_goals = models.IntegerField(blank=True, null=True)
    DEF_clearance_off_line = models.IntegerField(blank=True, null=True)
    DEF_outfielder_block = models.IntegerField(blank=True, null=True)

    # Goalkeeping Actions (KAL)
    KAL_good_high_claim = models.IntegerField(blank=True, null=True)
    KAL_saved_shots_from_inside_the_box = models.IntegerField(blank=True, null=True)
    KAL_saves = models.IntegerField(blank=True, null=True)
    KAL_punches = models.IntegerField(blank=True, null=True)
    KAL_total_keeper_sweeper = models.IntegerField(blank=True, null=True)
    KAL_accurate_keeper_sweeper = models.IntegerField(blank=True, null=True)
    KAL_goals_prevented = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    KAL_penalty_save = models.IntegerField(blank=True, null=True)
    KAL_penalty_shootout_save = models.IntegerField(blank=True, null=True)
    KAL_penalty_shootout_goal = models.IntegerField(blank=True, null=True)
    KAL_penalty_shootout_miss = models.IntegerField(blank=True, null=True)

    # Match and Team Information
    match_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    team = models.CharField(max_length=255, blank=True, null=True)

    # Other Statistics
    minutes_played = models.IntegerField(blank=True, null=True)
    touches = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    rating_original = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    rating_alternative = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    # Additional Player Information
    player_first_name = models.CharField(max_length=255, blank=True, null=True)
    player_last_name = models.CharField(max_length=255, blank=True, null=True)

    # Translations
    name_translation_ar = models.CharField(max_length=255, blank=True, null=True)
    short_name_translation_ar = models.CharField(max_length=255, blank=True, null=True)

    # Captain Information
    captain = models.BooleanField(default=False)

    # Meta sınıfı ile eşsiz kısıtlama
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['match_id', 'player_id'], name='unique_match_player')
        ]

    def __str__(self):
        return f"{self.player_name} - {self.team_name}"





