from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('hapus/<str:kode>', views.hapus, name="hapus" ),
    path('edit/<str:kode>', views.edit, name="edit" ),
]
