# -*-coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):

    titulo = models.CharField('Titulo', max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.titulo


class Post(models.Model):

    titulo = models.CharField('Titulo', max_length=50)
    conteudo = models.TextField('Conteúdo')
    categoria = models.ForeignKey(Categoria)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.titulo
