from __future__ import unicode_literals

from django.db import models

class Curso(models.Model):

    Nome = models.CharField(max_length=50)
    duracao = models.IntegerField()
    faculdade = models.CharField(max_length=50)
    imgLink = models.CharField(max_length=200,default='http://images.hacktabs.com//2012/07/404-not-found.gif')

    def __str__(self):
        return self.Nome


class Cadeira(models.Model):
    Curso =  models.ForeignKey(Curso,on_delete=models.CASCADE)
    Nome = models.CharField(max_length=50)
    Ano = models.IntegerField()
    descricao = models.TextField(default="Description")
    autor = models.CharField(max_length=50,default="Renato Dinis")
    imgLink = models.CharField(max_length=200, default='http://images.hacktabs.com//2012/07/404-not-found.gif')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.Nome

class Tema(models.Model):
    Cadeira = models.ForeignKey(Cadeira,on_delete=models.CASCADE)
    Nome =  models.CharField(max_length=100)
    Texto = models.TextField()

    def __str__(self):
        return self.Nome

class SubTema(models.Model):

    Tema =  models.ForeignKey(Tema, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=100)
    Texto = models.TextField()

    def __str__(self):
        return self.Nome

