from django import forms
from .models import Reg,Payment

States=[
    ('AP','AP'),
    ('Telangana','Telangana'),
    ('UP','UP'),
    ('Kerala','Kerala'),
    ]
Mandals=[
    ('Allagadda','Allagadda'),
    ('kadapa','kadapa'),
    ('Guntur','Guntur'),
    ('Koilakuntla','koilakuntla'),
    ]
Villages=[
    ('Ahobilam','Ahobilam'),
    ('Dorasi','Dorasi'),
    ('Suryapet','Suryapet'),
    ('Orvakal','Orvakal'),
    ]


class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields='__all__'

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)


class LocationForm(forms.Form):
    States=forms.CharField(label='select the States',widget=forms.Select(choices=States))
    Mandals=forms.CharField(label='select the Mandals',widget=forms.Select(choices=Mandals))
    Villages=forms.CharField(label='select the Villages',widget=forms.Select(choices=Villages))
    

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields='__all__'
        
    
