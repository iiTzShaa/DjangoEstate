from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),  # Corrected to use 'index'
    path('<int:listing_id>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]