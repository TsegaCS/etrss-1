from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
from .models import latlng
from django.core.mail import EmailMessage

from . import forms
from mapapp.forms import MapForm


def home(request):
    return render(request, 'accounts/dashboard.html')

# def map(request):
#     form = MapForm()
#     if request.method == "POST":
#         form = MapForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return home(request)
#         else:
#             print('ERROR! FORM INVALID')

#     return render(request, 'maps/map.html', {'form': form})

def map(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        organization = request.POST.get('organization')
        # request_date = request.POST.get('request_date')
        contact_person = request.POST.get('contact_person')
        applicationField = request.POST.get('applicationField')
        orderType = request.POST.get('orderType')
        productLevel = request.POST.get('productLevel')
        delivery_media = request.POST.get('delivery_media')
        data_format = request.POST.get('data_format')
        satellite_source = request.POST.get('satellite_source')
        cloud_cover = request.POST.get('cloud_cover')
        nto_additional_descriptions = request.POST.get('nto_additional_descriptions')
        aoi_additional_descriptions = request.POST.get('aoi_additional_descriptions')
        confirmation_email = request.POST.get('confirmation_email')
        # latitude = request.POST.get('latitude')
        # longitude = request.POST.get('longitude')

        kmlKmz = request.FILES.get('kmlKmz', "KML")
        shapeFile = request.FILES.get('shapeFile', "SHAPE")

        # todo: Do some validations up in here.

        req = latlng(latitude=latitude, longitude=longitude, organization=organization, contact_person=contact_person, applicationField=applicationField, satellite_source=satellite_source, orderType=orderType, productLevel=productLevel, delivery_media=delivery_media, data_format=data_format, cloud_cover=cloud_cover, nto_additional_descriptions=nto_additional_descriptions, aoi_additional_descriptions=aoi_additional_descriptions,  kmlKmz=kmlKmz, shapeFile=shapeFile, confirmation_email=confirmation_email)

        # fs = FileSystemStorage()
        # fs2 = FileSystemStorage()
        # fs.save(kmlKmz.name, kmlKmz)
        # fs2.save(shapeFile.name, shapeFile)

        req.save()

        # Avoid Duplications

        # Send email

        # msg = EmailMessage(
        #     'ETRSS-1 Satellite Product Inquiry',
        #     '<h3>Dear Mr./Mrs. ' + contact_person + ',</h3> Your ETRSS-1 Satellite Product Inquiry is under review and we will contact you soon. <br><br> <i>Meanwhile, here are your request details:</i> <br><br> Latitude: <b>' + latitude + '</b><br> Longitude: <b>'+ longitude+'</b><br> Application Field: <b>' + applicationField + '</b><br> Order Type: <b>' + orderType + '</b><br> Product Level: <b>' + productLevel+'</b><br> Delivery Media: <b>'+delivery_media+'</b><br> Data Format: <b>'+data_format+'</b><br>Satellite Source: <b>' +satellite_source+'</b><br> Cloud Cover: <b>'+cloud_cover+'</b><br> NTO Special Request: <b>'+nto_additional_descriptions+'</b><br> AOI Additional Request: <b>'+aoi_additional_descriptions+'</b><br><br> <h1>Thank you for Choosing ETRSS-1!</h1>',
        #     'tsegupower@gmail.com',
        #     [confirmation_email, 'tsegupower@gmail.com'],
        # )
        # msg.content_subtype="html"
        # msg.send()

        #TODO: ADD THREE ADMINS MAIL TO BE SENT

        messages.success(request, "Your request has been submitted! You will receive a confirmation email from ESSTI shortly.")
        # return redirect
        # string = [
        #     "Your request has been submitted! ESSTI will get back to you soon shortly. Thank you for choosing ETRSS-1!"]
        # return render(request, 'maps/map.html', {'string': string})
        return render(request, 'accounts/dashboard.html')

    return render(request, 'maps/map.html')


## return render(request, 'accounts/dashboard.html')

## return render(request, 'archives/archiverequest.html', context)


# TODo: concatinate messages when redirecting in other pages
