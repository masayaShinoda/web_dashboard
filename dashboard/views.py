import psutil
from django.shortcuts import render

def get_system_stats():
    return {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'ram_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
    }

def system_stats_view(request):
    return render(request, 'dashboard/system_stats.html')

def system_stats_partial(request):
    context = get_system_stats()
    return render(request, 'dashboard/system_stats_table.html', context)
