from django.conf import settings
from django.db import models

class Cargo(models.Model):
	id_cargo = models.AutoField(primary_key=True)
	nome_cargo = models.CharField(max_length=30) 
	descricao_cargo = models.TextField()

	def __str__(self):
		return self.nome_cargo

class Vaga(models.Model):
	id_vaga = models.AutoField(primary_key=True)
	nome_vaga = models.CharField(max_length=30) 
	descricao_vaga = models.TextField()
	salario = models.CharField(max_length=10)
	cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)

	def __str__(self):
		return self.nome_vaga

class Candidato(models.Model):
	nome_candidato = models.CharField(max_length=30) 
	curriculo = models.FileField(upload_to='curriculos/')
	vaga = models.ForeignKey(Vaga,on_delete=models.CASCADE)





