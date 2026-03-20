from django import forms
from .models import Cliente, Restaurante, Repartidor, Pedido


#cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion', 'activo']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
        }

    #Validaciones
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if not telefono.isdigit():
            raise forms.ValidationError("El telefono solo debe contener nuúmeros")
        
        if len(telefono) != 10:
            raise forms.ValidationError("El telefono debe tener 10 digitos")
        
        return telefono

class RestauranteForm(forms.ModelForm):
    class Meta:
        model  = Restaurante
        fields = ['nombre', 'direccion', 'telefono', 'categoria', 'activo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if not telefono.isdigit():
            raise forms.ValidationError("El telefono solo debe contener nuúmeros")
        
        if len(telefono) != 10:
            raise forms.ValidationError("El telefono debe tener 10 digitos")
        
        return telefono

        


class RepartidorForm(forms.ModelForm):
    class Meta:
        model  = Repartidor
        fields = ['nombre', 'telefono', 'vehiculo', 'disponible', 'activo']
     
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")
        return nombre
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')

        if not telefono.isdigit():
            raise forms.ValidationError("El telefono solo debe contener nuúmeros")
        
        if len(telefono) != 10:
            raise forms.ValidationError("El telefono debe tener 10 digitos")
        
        return telefono


class PedidoForm(forms.ModelForm):
    class Meta:
        model  = Pedido
        fields = ['cliente', 'restaurante', 'repartidor', 'descripcion', 'total', 'propina', 'status']
    
    def clean_total(self):
        total = self.cleaned_data.get('total')
        if total <= 0:
            raise forms.ValidationError("El total deve ser mayor a 0")
        return total
    
    def clean_propina(self):
        propina = self.cleaned_data.get('propina')

        if not propina:
            return '0'

        try:
            propina_int = int(propina)
        except ValueError:
            raise forms.ValidationError("Valor de propina inválido")

        if propina_int < 0 or propina_int > 100:
            raise forms.ValidationError("La propina debe estar entre 0 y 100%")

        return propina
    