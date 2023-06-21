from django.shortcuts import render
from django.db.models import Count

from records.models import Record

def home(request):
    sleep_mode = Record.objects.values('sleep').annotate(mode_count=Count('sleep')).order_by('-mode_count').first()
    yoga_mode = Record.objects.values('yoga').annotate(mode_count=Count('yoga')).order_by('-mode_count').first()
    gym_mode = Record.objects.values('gym').annotate(mode_count=Count('gym')).order_by('-mode_count').first()
    walking_mode = Record.objects.values('walking').annotate(mode_count=Count('walking')).order_by('-mode_count').first()
    reading_mode = Record.objects.values('reading').annotate(mode_count=Count('reading')).order_by('-mode_count').first()
    skills_development_mode = Record.objects.values('skills_development').annotate(mode_count=Count('skills_development')).order_by('-mode_count').first()
    water_intake_mode = Record.objects.values('water_intake').annotate(mode_count=Count('water_intake')).order_by('-mode_count').first()

    context = {
        'sleep_mode': f"{sleep_mode['sleep']} hours" if sleep_mode else None,
        'yoga_mode': f"{yoga_mode['yoga']} mins" if yoga_mode else None,
        'gym_mode': f"{gym_mode['gym']} mins" if gym_mode else None,
        'walking_mode': f"{walking_mode['walking']} mins" if walking_mode else None,
        'reading_mode': f"{reading_mode['reading']} mins" if reading_mode else None,
        'skills_development_mode': f"{skills_development_mode['skills_development']} mins" if skills_development_mode else None,
        'water_intake_mode': f"{water_intake_mode['water_intake']} ml" if water_intake_mode else None
    }

    return render(request, 'home.html', context)
