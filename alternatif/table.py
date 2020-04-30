from django import forms
from .models import alternatif
class formtabel(forms.ModelForm):
    class Meta:
        model = alternatif
        fields = ['kodealternatif', 'namaalternatif', 'c1','c2','c3','c4','c5']
        widgets = {
            'kodealternatif': forms.TextInput(attrs={'class':'form-control', 'placeholder':'KODE ALTERNATIF'}),
            'namaalternatif': forms.TextInput(attrs={'class':'form-control', 'placeholder':'NAMA ALTERNATIF'}),
            'c1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'JUTA Rp.'}),
            'c2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'%'}),
            'c3': forms.Select(attrs={'class':'form-control', 'placeholder':'C3'}),
            'c4': forms.Select(attrs={'class':'form-control', 'placeholder':'C4'}),
            'c5': forms.Select(attrs={'class':'form-control', 'placeholder':'C5'}),            
        }
        labels ={
            'kodealernatif':'KODE',
            'namaalternatif':'NAMA',
            'c1':'C1',
            'c2':'C2',
            'c3':'C3',
            'c4':'C4',
            'c5':'C5',
        }
    