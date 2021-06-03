from django.db import models

'''
    Tipos de datos para los campos de los modelos:
    - Todos los campos se obtienen de models
    -> CharField(max_lenght=25, default='Jack', null=True, blank=True)
    -> TextField()
    -> IntegerField()
    -> DecimalField(max_digits=5, decimal_places=2)
    -> PositiveIntegerField()
    -> SmallIntegerField()
    -> BooleanField(default=True)
    -> EmailField()
    -> ImageField(upload_to='fotos')
    -> FileField(upload_to='archivos')
    -> SlugField(): Tesla ha afectado el precio del Bitcoin >> tesla-ha-afectado-....

    Campos para establecer relaciones entre Modelos:
    -> ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    -> OneToOneField()
    -> ManyToManyField()

'''

class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    experiencia = models.TextField()

    def __str__(self):
        return self.nombre


class Conferencia(models.Model):
    nombre = models.CharField(max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    conferencista = models.ForeignKey(Conferencista, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Conferencia; {self.nombre} - Conferencista: {self.conferencista}'


class Participante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    twitter = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    



