from django.shortcuts import render, redirect
from .models import Plant, Fertilizer
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import WateringForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class PlantList(LoginRequiredMixin, ListView):
    model = Plant

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

class PlantDetail(LoginRequiredMixin, DetailView):
    model = Plant

    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     fertilizer_plant_doesnt_have = Fertilizer.objects.exclude(id__in = self.object.fertilizers.all().values_list('id'))
     context['watering_form'] = WateringForm()
     context ['fertilizers'] = fertilizer_plant_doesnt_have
     return context

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = fields = ['name', 'species', 'description', 'age']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['species', 'description', 'age']

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = reverse_lazy('plant-index')

@login_required
def add_watering(request, pk):
    form = WateringForm(request.POST)
    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.plant_id = pk
        new_watering.save()
    return redirect('plant-detail', pk=pk)

class FertilizerCreate(LoginRequiredMixin, CreateView):
    model = Fertilizer
    fields = '__all__'

class FertilizerList(LoginRequiredMixin, ListView):
    model = Fertilizer

class FertilizerDetail(LoginRequiredMixin, DetailView):
    model = Fertilizer

class FertilizerUpdate(LoginRequiredMixin, UpdateView):
    model = Fertilizer
    fields = ['name', 'fert_type', 'color']

class FertilizerDelete(LoginRequiredMixin, DeleteView):
    model = Fertilizer
    success_url = reverse_lazy('fertilizer-index')

@login_required
def associate_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.add(fertilizer_id)
    return redirect('plant-detail', pk=plant_id)


@login_required
def remove_fertilizer(request, plant_id, fertilizer_id):
    Plant.objects.get(id=plant_id).fertilizers.remove(fertilizer_id)
    return redirect('plant-detail', pk=plant_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plant-index')
        else:
            error_message = 'Invalid sign up - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
  
    
