from django.urls import path
from .views import system_stats_view, system_stats_partial

urlpatterns = [
    path('', system_stats_view, name='system_stats'),
    path('stats/partial/', system_stats_partial, name='system_stats_partial'),
]
