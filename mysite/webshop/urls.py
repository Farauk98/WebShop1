from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('paintings/', views.PaintingsView.as_view(), name='paintings'),
    path('artists/', views.ArtistsView.as_view(), name='artists'),
    path('paintings/create/', views.PaintingsCreateView.as_view(), name='create-paintings'),
    path('artists/create/', views.ArtistsCreateView.as_view(), name='create-artists'),
    path('delete/<str:object_type>/<int:object_id>/', views.ObjectDeleteView.as_view(), name='delete-object'),
    path('artists/select/', views.ArtistSelectView.as_view(), name='select-artists'),
    path('paintings/select/', views.PaintingSelectView.as_view(), name='select-paintings'),
]