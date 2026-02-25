from django.shortcuts import render, redirect
from .models import Plant, Fertilizer
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import WateringForm


# Create your views here.
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class PlantList(ListView):
    model = Plant

class PlantDetail(DetailView):
    model = Plant

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     fertilizer_plant_doesnt_have = Fertilizer.objects.exclude(id__in = self.object.fertilizers.all().values_list('id'))
     context['watering_form'] = WateringForm()
     context ['fertilizers'] = fertilizer_plant_doesnt_have
     return context

class PlantCreate(CreateView):
    model = Plant
    fields = fields = ['name', 'species', 'description', 'age']

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'description', 'age']

class PlantDelete(DeleteView):
    model = Plant
    success_url = reverse_lazy('plant-index')

def add_watering(request, pk):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = pk
        new_watering.save()
    return redirect('plant-detail', pk=pk)

class FertilizerCreate(CreateView):
    model = Fertilizer
    fields = '__all__'

class FertilizerList(ListView):
    model = Fertilizer

class FertilizerDetail(DetailView):
    model = Fertilizer

class FertilizerUpdate(UpdateView):
    model = Fertilizer
    fields = ['name', 'fert_type', 'color']

class FertilizerDelete(DeleteView):
    model = Fertilizer
    success_url = reverse_lazy('fertilizer-index')


def associate_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
    return redirect('plant-detail', pk=plant_id)



def remove_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
    return redirect('plant-detail', pk=plant_id)