from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
import random

def index(request):
    return render(request, "dashboard/index.html")

def tabla(request):
    # Simulación de datos analíticos
    
    clientes = ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D']
    metricas = ['Métrica 1', 'Métrica 2', 'Métrica 3', 'Métrica 4']
    
    data = []
    for i in range(10):
        
        fila = {
            "fecha": (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d"),
            "cliente": random.choice(clientes),
            "metrica": random.choice(metricas),
            "valor": random.randint(100, 1000)
        }
        data.append(fila)
    return render(request, 'dashboard/tabla.html', {'data': data})