from django.db import models
from datetime import date

class Score(models.Model):
    record = models.OneToOneField('Record', on_delete=models.CASCADE, primary_key=True)
    sleep_score = models.IntegerField(default=0)
    yoga_score = models.IntegerField(default=0)
    gym_score = models.IntegerField(default=0)
    walking_score = models.IntegerField(default=0)
    reading_score = models.IntegerField(default=0)
    skills_development_score = models.IntegerField(default=0)
    water_intake_score = models.IntegerField(default=0)

class Record(models.Model):
    # Primary Key
    recordid = models.CharField(max_length=8, primary_key=True, editable=False)

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
        ('3L','3L scores 3'),
        ('2L','3L scores 2'),
        ('1L','3L scores 1'),
    ]

    sleep = models.CharField(max_length=4, choices=SLEEP_CHOICES)
    yoga = models.CharField(max_length=4, choices=CHOICES)
    gym = models.CharField(max_length=4, choices=CHOICES)
    walking = models.CharField(max_length=4, choices=CHOICES)
    reading = models.CharField(max_length=4, choices=CHOICES)
    skills_development = models.CharField(max_length=4, choices=CHOICES)
    water_intake = models.CharField(max_length=4, choices=WATER_CHOICES)
    expenses = models.IntegerField()
    todays_dairy = models.TextField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_scores(self):
        score_mapping = {
            '1-3': 15,
            '3-5': 10,
            '5-7': 5,
            '7+': 0,
            '60': 10,
            '45': 5,
            '30': 2,
            '15': 1,
            '0':0,
            '3L':3,
            '2L':2,
            '1L':1
        }

        score = Score.objects.get_or_create(record=self)[0]
        score.sleep_score = score_mapping.get(self.sleep, 0)
        score.yoga_score = score_mapping.get(self.yoga, 0)
        score.gym_score = score_mapping.get(self.gym, 0)
        score.walking_score = score_mapping.get(self.walking, 0)
        score.reading_score = score_mapping.get(self.reading, 0)
        score.skills_development_score = score_mapping.get(self.skills_development, 0)
        score.water_intake_score = score_mapping.get(self.water_intake, 0)
        score.save()

    def save(self, *args, **kwargs):
        # Generate recordid based on the current date
        if not self.recordid:
            self.recordid = date.today().strftime('%Y%m%d')

        super().save(*args, **kwargs)  # Save the record first

        # Calculate and update the scores
        self.calculate_scores()

    def __str__(self):
        return self.recordid
