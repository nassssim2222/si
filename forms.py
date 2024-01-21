from dateutil.parser import parse
from datetime import datetime
from http import client
from django.db.models import fields
from django import forms


from .models import achats, achats_tranche, centre_pv, emprunt, fournisseur, matiere_premiere, produit, pvs, team, client, transferer, ventes, ventes_tranche

class productform(forms.ModelForm):
    class Meta:
        model = produit
        fields="__all__"

class centerform(forms.ModelForm):
    class Meta:
        model = centre_pv
        fields="__all__"        


class clientform(forms.ModelForm):
    class Meta:
        model = client
        fields="__all__"        

class fournisseurform(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields="__all__"        


class matiereform(forms.ModelForm):
    class Meta:
        model = matiere_premiere
        fields="__all__"        


class teamform(forms.ModelForm):
    class Meta:
        model = team
        fields="__all__"     

class achatsform(forms.ModelForm):
    class Meta:
        model = achats
        fields="__all__"      

class trancheform(forms.ModelForm):
    class Meta:
        model = achats_tranche
        fields="__all__"

class regler_fournisseur_form(forms.ModelForm):
    class Meta:
        model = fournisseur
        fields = ["fournisseur_SOLD"]

class transfereform(forms.ModelForm):
    class Meta:
        model = transferer
        fields = "__all__"

class venteform(forms.ModelForm):
    class Meta:
        model = ventes
        fields = "__all__"

class trancheform1(forms.ModelForm):
    class Meta:
        model = ventes_tranche
        fields="__all__"

class regler_client_form(forms.ModelForm):
    class Meta:
        model = client
        fields = ["client_credit"]


class FiltreStockForm(forms.Form):
    fournisseur = forms.ModelChoiceField(queryset=fournisseur.objects.all(), required=False)
    date_achat = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    def clean_date_achat(self):
        date_achat = self.cleaned_data.get('date_achat')
        
        # Utiliser strptime pour convertir la chaîne en objet de date
        try:
            return datetime.strptime(date_achat, '%Y-%m-%d').date()
        except ValueError:
            return None
    


class PointageForm(forms.Form):
    employer_Present = forms.BooleanField(required=False, initial=False)
    #employer_absent = forms.BooleanField(required=False, initial=False)


class empruntform(forms.ModelForm):
    class Meta:
        model = emprunt
        fields = "__all__"

class teamform(forms.ModelForm):
    class Meta:
        model = team
        fields="__all__"    

class pvform(forms.ModelForm):
    class Meta:
        model = pvs
        fields = "__all__"