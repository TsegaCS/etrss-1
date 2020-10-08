from django import forms
from django.core import validators
from mapapp.models import latlng


class MapForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    class Meta():
        model = latlng
        fields = "__all__"

    # latitude = forms.FloatField()
    # longitude = forms.FloatField()
    #
    # organization = forms.CharField()
    # place_name = forms.CharField()
    #
    # request_date = forms.DateTimeField()
    #
    # applicationField = forms.CharField()
    # orderType = forms.CharField()
    # productLevel = forms.CharField()
    # delivery_media = forms.CharField()
    # # surface = forms.CharField(, )
    # kmlKmz = forms.FileField()
    # shapeFile = forms.FileField()
    # data_format = forms.CharField()
    # satellite_source = forms.CharField()
    # cloud_cover = forms.CharField()
    # nto_additional_descriptions = forms.CharField(widget=forms.Textarea)
    # aoi_additional_descriptions = forms.CharField()
    # confirmation_email = forms.CharField()
    # contact_person = forms.CharField()
