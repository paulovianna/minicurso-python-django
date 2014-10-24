from django.db import models

class Post(models.Model):

    titulo = models.CharField('Titulo', max_length=50)
    conteudo = models.TextField('Conteudo')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.titulo
    
