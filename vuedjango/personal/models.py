from django.db import models


class Autor(models.Model):
    documento = models.BigIntegerField()
    nombre = models.CharField(max_length=200)
    fecha_naci = models.DateField()

    def __str__(self):
        return self.nombre


class Choice(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    def nombreAutor(self):
        return self.autor.nombre