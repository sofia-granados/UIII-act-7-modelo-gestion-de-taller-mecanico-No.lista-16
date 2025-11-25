
     from django.db import models

    class Cliente_Taller(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=255)
    dni = models.CharField(max_length=20)
    fecha_registro = models.DateField()
    preferencia_contacto = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Vehiculo_Taller(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    matricula = models.CharField(max_length=20)
    num_chasis = models.CharField(max_length=50)
    id_cliente = models.ForeignKey(Cliente_Taller, on_delete=models.CASCADE)
    kilometraje_entrada = models.IntegerField()
    color = models.CharField(max_length=20)
    fecha_recepcion = models.DateTimeField()
    estado_general = models.TextField()

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.matricula}"

class Mecanico(models.Model):
    id_mecanico = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    certificado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Orden_Reparacion(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_vehiculo = models.ForeignKey(Vehiculo_Taller, on_delete=models.CASCADE)
    fecha_recepcion = models.DateTimeField()
    fecha_salida_estimada = models.DateField()
    estado_orden = models.CharField(max_length=50)
    diagnostico_inicial = models.TextField()
    costo_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    id_mecanico_asignado = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    observaciones = models.TextField()

    def __str__(self):
        return f"Orden {self.id_orden} - {self.id_vehiculo}"

class Repuesto(models.Model):
    id_repuesto = models.AutoField(primary_key=True)
    nombre_repuesto = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_proveedor_repuesto = models.IntegerField()
    num_pieza_fabricante = models.CharField(max_length=50)
    compatibilidad_vehiculos = models.TextField()

    def __str__(self):
        return self.nombre_repuesto

class Detalle_Reparacion(models.Model):
    id_detalle_rep = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden_Reparacion, on_delete=models.CASCADE)
    id_repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad_repuesto = models.IntegerField()
    precio_repuesto_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    mano_obra_horas = models.DecimalField(max_digits=5, decimal_places=2)
    costo_mano_obra_hora = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_item = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id_detalle_rep} - Orden {self.id_orden}"

class Factura_Taller(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden_Reparacion, on_delete=models.CASCADE)
    fecha_emision = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=50)
    metodo_pago = models.CharField(max_length=50)
    fecha_vencimiento = models.DateField()
    id_cliente_factura = models.ForeignKey(Cliente_Taller, on_delete=models.CASCADE)
    iva_aplicado = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id_factura} - {self.id_orden}"
