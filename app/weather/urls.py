from django.urls import path
from .views import destroy_view, index_view, create_view

app_name = 'weather'

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', create_view, name='create'),
    path('del/<pk>/', destroy_view, name='destroy'),
]