from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('paintings/', views.PaintingsView.as_view(), name='paintings'),
    path('artists/', views.ArtistsView.as_view(), name='artists'),
    path('paintings/create/', views.PaintingsCreateView.as_view(), name='create-paintings'),
    path('artists/create/', views.ArtistsCreateView.as_view(), name='create-artists'),
]