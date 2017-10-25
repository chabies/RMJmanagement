from django.contrib.gis import forms
from . import models
from django.contrib.gis.geos import Point

class AddProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            'name',
            'description',
            'stock',
            'weight',
            'order',
            'latitude',
            'longitude',
        ]

    '''
    name = forms.CharField()
    description = forms.CharField()
    stock =forms.IntegerField()
    weight = forms.FloatField()
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    order = forms.IntegerField()'''



    '''
    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        required=True,
    )

    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        required=True,
    )

    
        widgets = {'location': forms.(srid=4326, widgets=forms.TextInputxt)}

    def clean(self):
        data = super(AddProduct,self).clean()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        location = data.get('location')
        if latitude and longitude and not location:
            data['location'] = Point(longitude, latitude)'''