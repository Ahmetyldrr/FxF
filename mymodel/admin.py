from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import TeamPerformance

# Modeli admin paneline ekle
@admin.register(TeamPerformance)
class TeamPerformanceAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'team_name_x', 'team_name_y', 'ATT_goals_x', 'ATT_goals_y', 'rating_x', 'rating_y')
    search_fields = ('match_id', 'team_name_x', 'team_name_y')
    list_filter = ('team_name_x', 'team_name_y')

# Burada 'list_display' kısmında admin panelinde hangi alanların görüneceğini belirttik.
