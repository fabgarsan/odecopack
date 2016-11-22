from datetime import datetime

from django.db import models


# Create your models here.

class VendedorBiable(models.Model):
    LINEAS = (
        (1, 'Proyectos'),
        (2, 'Bandas y Componentes'),
        (3, 'Posventa'),
        (4, 'Sin Definir'),
    )
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=200)
    linea = models.PositiveIntegerField(choices=LINEAS, default=4)

    def __str__(self):
        return self.nombre


class MovimientoVentaBiable(models.Model):
    id_vendedor = models.PositiveIntegerField()
    id_terc_fa = models.CharField(max_length=20)
    cliente = models.CharField(max_length=200)
    proyecto = models.CharField(max_length=10)
    item_id = models.PositiveIntegerField()
    precio_uni = models.DecimalField(max_digits=18, decimal_places=4)
    fecha = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=18, decimal_places=4)
    venta_bruta = models.DecimalField(max_digits=18, decimal_places=4)
    dscto_netos = models.DecimalField(max_digits=18, decimal_places=4)
    costo_total = models.DecimalField(max_digits=18, decimal_places=4)
    rentabilidad = models.DecimalField(max_digits=18, decimal_places=4)
    imp_netos = models.DecimalField(max_digits=18, decimal_places=4)
    venta_neto = models.DecimalField(max_digits=18, decimal_places=4)