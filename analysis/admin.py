from django.contrib import admin

from django.contrib import admin
from .models import MatchStats

from django.contrib import admin
from .models import MatchStats

# `MatchStats` modeli için özelleştirilmiş bir admin sınıfı oluşturuyoruz.
class MatchStatsAdmin(admin.ModelAdmin):
    # Admin panelinde listede görünecek alanlar
    list_display = ('id', 'tarih', 'update_date', 'stats_summary')
    
    # Admin panelinde filtreleme yapabileceğimiz alanlar
    list_filter = ('tarih', 'update_date')
    
    # Admin panelinde arama yapabileceğimiz alanlar
    search_fields = ('id', 'tarih')
    
    # Admin panelinde gösterilen JSON alanının özetini almak için özel bir metot
    def stats_summary(self, obj):
        # 'stats' alanındaki JSON verisinden bir özet döndürme
        if obj.stats:
            return str(obj.stats)[:300] + "..." if len(str(obj.stats)) > 10 else str(obj.stats)
        return "Veri yok"
    
    # Sütun başlığı için daha okunabilir bir isim
    stats_summary.short_description = 'İstatistik Özeti'

# `MatchStats` modelini ve `MatchStatsAdmin` sınıfını admin paneline ekliyoruz
admin.site.register(MatchStats, MatchStatsAdmin)
