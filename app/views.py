from django.shortcuts import render
from .models import Vaga

def vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'app/index.html', {'vagas': vagas})
