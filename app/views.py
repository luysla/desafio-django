from django.shortcuts import render
from .models import Vaga, Candidato
from .forms import CandidatoForm
from django.shortcuts import redirect

#def candidatos(request):
#   candidatos = Candidato.objects.all()
#    return render(request, 'app/index.html', {'candidato': candidato})

def index(request):
	candidatos = Candidato.objects.all()	
	return render(request, 'app/index.html', {'candidatos': candidatos})

def novo_candidato(request):
	#form = CandidatoForm()
	vagas = Vaga.objects.all()

	form = CandidatoForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('index')
	else:
		form = CandidatoForm()
		return render(request, 'app/add_candidato.html', {'form': form, 'vagas': vagas})

	return render(request, 'app/add_candidato.html', {'form': form, 'vagas': vagas})

	
	
     	