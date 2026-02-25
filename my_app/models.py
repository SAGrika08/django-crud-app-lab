from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

TYPES = (
    ('L', 'Liquid'),
    ('O', 'Organic'),
    ('S', 'Slow-Release'),
)

class Fertilizer(models.Model):
    name = models.CharField(max_length=50)
    fert_type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.get_fert_type_display()})"

    def get_absolute_url(self):
        return reverse('fertilizer-detail', kwargs={'pk': self.id})




class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    fertilizers = models.ManyToManyField(Fertilizer)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('plant-detail', kwargs={'pk': self.id}) 
    
    def water_for_today(self):
        return self.watering_set.filter(date=date.today()).count() >= len(TIMES)



class Watering(models.Model):
    date = models.DateField('Watering date')
    time_of_day = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_of_day_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    
