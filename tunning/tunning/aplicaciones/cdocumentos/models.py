from django.db import models

# Create your models here.
class Pat_cdoc_parametros(models.Model):
    ruta_temporal = models.CharField(max_length=300)
    ruta_defitiva = models.CharField(max_length=300)
    

class proyectos_consulta(models.Model):
     CodigoProyecto = models.CharField(primary_key=True, max_length=50)
     Nombre = models.CharField(max_length=50)
     Descripcion = models.CharField(max_length=50)
     CodiCC = models.CharField(max_length=50)
     NomAux = models.CharField(max_length=50)
     Id_usuario = models.IntegerField()

     class Meta:
         managed = False
         db_table = 'PAv_CDOC_Proyectos'  # Nombre de la vista en la base de datos
         
class consulta_proyecto_doc(models.Model):
    CodigoProyecto  = models.CharField(primary_key=True, max_length=50)
    Nombre          = models.CharField(max_length=200)
    Descripcion     = models.CharField(max_length=200)
    NomAux          = models.CharField(max_length=200)
    id_jefe_proyecto= models.IntegerField()
    Total_documento = models.IntegerField()
    transmittal_ing = models.IntegerField()
    transmittal_ot  = models.IntegerField()
    
    class Meta:
            managed = False
            db_table = 'Pav_CDOC_Proyectos_documentos'  # Nombre de la vista en la base de datos
        
class Listado_personal(models.Model):
    id          = models.IntegerField(primary_key=True)
    ficha       = models.IntegerField()
    nombre      = models.CharField(max_length=255)
    appaterno   = models.CharField(max_length=255)
    DesArn      = models.CharField(max_length=255)
    carNom      = models.CharField(max_length=255)

    class Meta:
        managed = False  # Indica que este modelo no debe ser gestionado por Django
        db_table = 'PAV_cdoc_Office365'  # Nombre de la vista SQL en la base de datos

        
class Pat_cdoc_header_proyectos(models.Model):
    opciones_dias = [
        (7, '7 días'),
        (10, '10 días'),
        (12, '12 días'),
        (15, '15 días'),
        (20, '20 días'),
        # Agrega más opciones según tus necesidades
    ]
    
    CodigoProyecto      = models.CharField(max_length=10, null=True, blank=False)
    id_jefe_proyecto    = models.IntegerField(null=True)
    dia_entrega_doc     = models.IntegerField(choices=opciones_dias, default=10)
    personal_contacto   = models.CharField(max_length=80, null=True)
    email_persona       = models.EmailField(max_length=254, null=True)
    fecha_creacion      = models.DateTimeField(auto_now_add=True)
    Total_documento     = models.SmallIntegerField(null=True,blank=True)
    transmittal_ing     = models.SmallIntegerField(null=True,blank=True)
    transmittal_ot      = models.SmallIntegerField(null=True,blank=True)
    

    def __str__(self):
        return f"{self.CodigoProyecto} - {self.id_jefe_proyecto}"
    
class Pat_cdoc_det_proyectos(models.Model):
     CodigoProyecto  = models.CharField(max_length=10, null=False, blank=False)
     equipo_proyecto = models.CharField(max_length=150, null=True,blank=True)
     fecha_creacion  = models.DateTimeField(auto_now_add=True)

# class Pat_cdoc_det_proyectos(models.Model):
#     CodigoProyecto = models.ForeignKey(Pat_cdoc_header_proyectos, on_delete=models.CASCADE)
#     equipo_proyecto = models.CharField(max_length=36)  # Cambia la longitud según las necesidades
#     fecha_creacion = models.DateTimeField(auto_now_add=True)
    

class Pat_cdoc_listado(models.Model):
    CodigoProyecto      =models.CharField(max_length=10, null=False, blank=False)
    cod_plano_tunning   =models.CharField(max_length=30,null=False,blank= False)
    cod_plano_Cliente   =models.CharField(max_length=30,null=True,blank= True)
    descripcion_plano   =models.CharField(max_length=100,null=True,blank= True)
    tipo_documento      =models.CharField(max_length=30,null=True,blank= True)
    Ult_rev_plano       =models.CharField(max_length=1, null=True, blank=True, default='I')
    fecha_creacion      =models.DateTimeField(auto_now_add=True)
    fecha_entrega       =models.DateField(null=True,blank= True)
    
    
    
class Pat_cdoc_mov_documento(models.Model):
    CodigoProyecto      =models.CharField(max_length=10, null=False, blank=False)
    codigo_transmittal  =models.CharField(max_length=18, null=False, blank=False)
    cod_plano_tunning   =models.CharField(max_length=30,null=False,blank= False)
    cod_plano_Cliente   =models.CharField(max_length=30,null=True,blank= True)
    rev_plano           =models.CharField(max_length=1,null=True,blank= True)
    tip_documento       =models.CharField(max_length=1,null=True,blank= True)
    fecha_creacion      =models.DateTimeField(auto_now_add=True)
    
    
    