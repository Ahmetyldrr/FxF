
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
