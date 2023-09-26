from django import forms
from django.forms.widgets import HiddenInput
from .models import *


class ProyectoPersonaForm(forms.ModelForm):
    class Meta:
        model = Pat_cdoc_header_proyectos
        fields = (
            'CodigoProyecto',
            'dia_entrega_doc',
            'personal_contacto',
            'email_persona',
            'id_jefe_proyecto',
        )
        widgets = {
            'id_jefe_proyecto': forms.HiddenInput()  # Campo oculto
        }


    # Marcar el campo como no obligatorio
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_jefe_proyecto'].required = False
        
        # super(ProyectoPersonaForm, self).__init__(*args, **kwargs)
        # self.fields['CodigoProyecto'].widget.attrs.update({'disabled': 'disabled'})

class DetalleProyectoForm(forms.ModelForm):
    class Meta:
        model = Pat_cdoc_det_proyectos
        fields = (
            'CodigoProyecto',
            'equipo_proyecto'
        )

