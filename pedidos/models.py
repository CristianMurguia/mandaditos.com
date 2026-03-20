from django.db import models


class Cliente(models.Model):
    nombre    = models.CharField(max_length=100)
    email     = models.EmailField(unique=True)
    telefono  = models.CharField(max_length=15)
    direccion = models.TextField()
    activo    = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Restaurante(models.Model):
    nombre    = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono  = models.CharField(max_length=15)
    categoria = models.CharField(max_length=80)
    activo    = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Repartidor(models.Model):
    VEHICULO_CHOICES = [
        ('bicicleta', 'Bicicleta'),
        ('moto',      'Motocicleta'),
        ('auto',      'Automóvil'),
    ]
    nombre     = models.CharField(max_length=100)
    telefono   = models.CharField(max_length=15)
    vehiculo   = models.CharField(max_length=20, choices=VEHICULO_CHOICES)
    disponible = models.BooleanField(default=True)
    activo     = models.BooleanField(default=True)
    creado_en  = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('servido',   'Servido'),
        ('reparto',   'En Reparto'),
        ('entregado', 'Entregado'),
    ]
    PROPINA_CHOICES = [
    (0,  'Sin propina'),
    (10, '10%'),
    (15, '15%'),
    (20, '20%'),
    (25, '25%'),
    ]


    cliente     = models.ForeignKey(Cliente,     on_delete=models.PROTECT)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.PROTECT)
    repartidor  = models.ForeignKey(Repartidor,  on_delete=models.PROTECT, null=True, blank=True)
    descripcion = models.TextField()
    total       = models.DecimalField(max_digits=8, decimal_places=2)
    propina = models.IntegerField(choices=PROPINA_CHOICES, default=0)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendiente')
    creado_en   = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'Pedido #{self.pk} — {self.cliente}'
    
    def total_con_propina(self):
        try:
            propina = int(self.propina)
        except:
            propina = 0

        return round(self.total + (self.total * propina / 100), 2)