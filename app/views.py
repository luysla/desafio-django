from django.shortcuts import render

def crud_candidatos(request):
    return render(request, 'app/crud_candidatos.html', {})
