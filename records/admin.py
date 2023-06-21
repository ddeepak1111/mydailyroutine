from django.contrib import admin

from .models import Record,Score

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = ('recordid', 'sleep', 'yoga', 'gym', 'walking', 'reading', 'skills_development','water_intake', 'expenses', 'todays_dairy')
    
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('record','sleep_score','yoga_score','gym_score','walking_score','reading_score','skills_development_score','water_intake_score','get_total_score')
    
    def get_total_score(self, obj):
        score = Score.objects.get(record=obj)
        total_score = score.sleep_score + score.yoga_score + score.gym_score + score.walking_score + score.reading_score + score.skills_development_score
        return total_score
    
    get_total_score.short_description = 'Total Score'

admin.site.register(Record,RecordAdmin)
admin.site.register(Score,ScoreAdmin)