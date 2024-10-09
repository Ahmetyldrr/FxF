
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


