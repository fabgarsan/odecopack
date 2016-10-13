import math
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from proveedores.models import MargenProvedor
from utils.models import TimeStampedModel


# Create your models here.

# region Unidades de Medida
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "2. Unidades de Medida"

    def __str__(self):
        return self.nombre


# endregion

# region Productos
def productos_upload_to(instance, filename):
    basename, file_extention = filename.split(".")
    new_filename = "produ_perfil_%s.%s" % (basename, file_extention)
    return "%s/%s/%s" % ("productos", "foto_perfil", new_filename)


class ProductoQuerySet(models.QuerySet):
    def para_ensamble(self):
        return self.filter(activo_ensamble=True)

    def para_catalogo(self):
        return self.filter(activo_catalogo=True)

    def para_componentes(self):
        return self.filter(activo_componentes=True)

    def para_proyectos(self):
        return self.filter(activo_proyectos=True)
        #
        # def editors(self):
        #     return self.filter(role='E')


class ProductoActivosManager(models.Manager):
    def get_queryset(self):
        return ProductoQuerySet(self.model, using=self._db).filter(activo=True)

    def modulos(self):
        return self.get_queryset().para_ensamble()

    def catalogo(self):
        return self.get_queryset().para_catalogo()

    def componentes(self):
        return self.get_queryset().para_componentes()

    def proyectos(self):
        return self.get_queryset().para_proyectos()


class Producto(TimeStampedModel):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 1.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    id_cguno = models.PositiveIntegerField(default=0)
    referencia = models.CharField(max_length=120, unique=True)
    descripcion_estandar = models.CharField(max_length=200)
    descripcion_comercial = models.CharField(max_length=200)
    fabricante = models.CharField(max_length=120, default="")
    cantidad_empaque = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT, null=True)
    cantidad_minima_venta = models.DecimalField(max_digits=18, decimal_places=4, default=0)

    margen = models.ForeignKey(MargenProvedor, null=True, blank=True, related_name="productos_con_margen",
                               verbose_name="Id MxC")
    costo = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    costo_cop = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    precio_base = models.DecimalField(max_digits=18, decimal_places=4, default=0)
    rentabilidad = models.DecimalField(max_digits=18, decimal_places=4, default=0)

    activo = models.BooleanField(default=True)
    activo_componentes = models.BooleanField(default=True, verbose_name="En Compo.")
    activo_proyectos = models.BooleanField(default=True, verbose_name="En Proy.")
    activo_catalogo = models.BooleanField(default=True, verbose_name="En Cata.")
    activo_ensamble = models.BooleanField(default=False, verbose_name="Para Ensam.")

    foto_perfil = models.ImageField(upload_to=productos_upload_to, validators=[validate_image], null=True, blank=True)
    created_by = models.ForeignKey(User, editable=False, null=True, blank=True, related_name="servicio_created")
    updated_by = models.ForeignKey(User, editable=False, null=True, blank=True, related_name="servicio_updated")

    objects = models.Manager()
    activos = ProductoActivosManager()

    class Meta:
        verbose_name_plural ="1. Productos"

    def __init__(self, *args, **kwargs):
        super(Producto, self).__init__(*args, **kwargs)
        self.precio_base_original = self.precio_base
        self.costo_original = self.costo

    def save(self, **kwargs):

        margen = kwargs.get("margen_deseado")
        factor_importacion = kwargs.get("factor_importacion")
        tasa = kwargs.get("tasa")

        if not tasa and not factor_importacion and not margen and self.costo != self.costo_original:
            print("en save Cambio Costo")
            self.set_precio_base_y_costo()
        if tasa or factor_importacion or margen:
            print("en save cambio otros")
            self.set_precio_base_y_costo(tasa=tasa, factor_importacion=factor_importacion, margen=margen)

        super().save()

        # Sólo entra a hacer el proceso de actualización de ensamblajes
        # si el precio base a cambiado
        if self.precio_base_original != self.precio_base:
            print("Entro a cambiar ensamblado")
            for ensamble in self.ensamblados.all():
                ensamble.save()

    def __str__(self):
        return "%s" % (self.descripcion_estandar)

    def set_precio_base_y_costo(self, tasa=None, factor_importacion=None, margen=None):

        if not tasa:
            print("Entro a buscar la tasa")
            tasa = self.margen.proveedor.moneda.moneda_cambio.cambio
        if not factor_importacion:
            print("Entro a buscar el factor")
            factor_importacion = self.margen.proveedor.factor_importacion
        if not margen:
            print("Entro a buscar el margen")
            margen = self.margen.margen_deseado
        margen = (margen) / 100  # Se transforma en porcentaje

        # Calculamos los nuevos costos y precios basados en el cambio de los parametros
        costo_base_cop = self.costo * tasa * factor_importacion
        self.costo_cop = costo_base_cop

        precio_base = costo_base_cop * (1 / (1 - margen))
        self.precio_base = round(precio_base, 4)

        self.rentabilidad = precio_base - costo_base_cop

# endregion
