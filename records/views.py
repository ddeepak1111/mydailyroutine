from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from records.forms import RecordForm
from django.db.models import Avg

from records.models import Record, Score
from django.contrib import messages

# Create your views here.

def progresscard(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'progresscard.html', context)

def addrecord(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record saved successfully.')
            return redirect(reverse('records:progresscard'))
    else:
        form = RecordForm()
    
    context = {'form': form}
    return render(request, 'todaysroutine.html', context)


def recorddetails(request, recordid):
    record = get_object_or_404(Record, recordid=recordid)
    score = Score.objects.get(record=record)
    avg_scores = Score.objects.aggregate(
        sleep_average=Avg('sleep_score'),
        yoga_average=Avg('yoga_score'),
        gym_average=Avg('gym_score'),
        walking_average=Avg('walking_score'),
        reading_average=Avg('reading_score'),
        skills_development_average=Avg('skills_development_score'),
        water_intake_average=Avg('water_intake_score')
    )
    context = {'record': record, 'score': score, 'avg_scores': avg_scores}
    return render(request, 'recorddetails.html', context)

