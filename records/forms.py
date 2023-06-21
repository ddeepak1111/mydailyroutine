from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    SLEEP_CHOICES = [
        ('1-3', '1 to 3 hours scores 15'),
        ('3-5', '3 to 5 hours scores 10'),
        ('5-7', '5 to 7 hours scores 5'),
        ('7+', 'Above 7 hours scores 0')
    ]

    CHOICES = [
        ('60', '60 mins scores 10'),
        ('45', '45 mins scores 5'),
        ('30', '30 mins scores 2'),
        ('15', '15 mins scores 1'),
        ('0','none')
    ]

    WATER_CHOICES = [
        ('3L', '3L scores 3'),
        ('2L', '2L scores 2'),
        ('1L', '1L scores 1'),
    ]

    sleep = forms.ChoiceField(choices=SLEEP_CHOICES)
    yoga = forms.ChoiceField(choices=CHOICES)
    gym = forms.ChoiceField(choices=CHOICES)
    walking = forms.ChoiceField(choices=CHOICES)
    reading = forms.ChoiceField(choices=CHOICES)
    skills_development = forms.ChoiceField(choices=CHOICES)
    water_intake = forms.ChoiceField(choices=WATER_CHOICES)

    class Meta:
        model = Record
        fields = '__all__'
