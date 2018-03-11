from django.urls import path
from Shortener import views




urlpatterns = [
    path('', views.shortener, name='main'),
    path('page_info/', views.display_urls, name='display_urls'),
    path('<int:pk>', views.redirecturl, name='new_short'),
]