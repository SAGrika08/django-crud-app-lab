from django.urls import path
from . import views 

urlpatterns = [
   path('', views.Home.as_view(), name='home'),
   path('about/', views.about, name='about'),
   path('plants/', views.PlantList.as_view(), name='plant-index'),
   path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plant-detail'),
   path('plants/create/', views.PlantCreate.as_view(), name='plant-create'),
   path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant-update'),
   path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant-delete'),
   path('plants/<int:pk>/add-watering/', views.add_watering, name='add-watering'),
   path('fertilizer/create/', views.FertilizerCreate.as_view(), name='fertilizer-create'),
   path('fertilizer/<int:pk>/', views.FertilizerDetail.as_view(), name='fertilizer-detail'),
   path('fertilizer/', views.FertilizerList.as_view(), name='fertilizer-index'),
   path('fertilizer/<int:pk>/update/', views.FertilizerUpdate.as_view(), name='fertilizer-update'),
   path('fertilizer/<int:pk>/delete/', views.FertilizerDelete.as_view(), name='fertilizer-delete'),
   path('plants/<int:plant_id>/associate-fertilizer/<int:fertilizer_id>/', views.associate_fertilizer, name='associate-fertilizer'),
   path('plants/<int:plant_id>/remove-fertilizer/<int:fertilizer_id>/', views.remove_fertilizer, name='remove-fertilizer'),
   path('accounts/signup/', views.signup, name='signup'),


]
