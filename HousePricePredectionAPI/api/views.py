from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, renderer_classes
from django.core import serializers
import joblib
import numpy as np
import pandas as pd
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import priceSerializers
from .models import price
from django.http import JsonResponse
from rest_framework import status
from .forms import PredictForm
from rest_framework.renderers import StaticHTMLRenderer
from django.contrib import messages


class PricePrediction(viewsets.ModelViewSet):
    queryset = price.objects.all()
    serializer_class = priceSerializers


@api_view(["GET"])
def index(request):
    return_data = {
        "error_code": "0",
        "info": "success",
    }
    return Response(return_data)


@api_view(["POST"])
def pricepredict(request):
    try:
        data=request.data
        # input_df = pd.DataFrame(np.array([data]).reshape(1, -1), columns=feature_names)
        price_info = np.array(list(data.values()))
        lin_reg_model = ApiConfig.model
        price_predicted = lin_reg_model.predict([price_info])
        price_predicted = int(price_predicted[0])
        response_dict = {
                         "Predicted price": price_predicted
                }
       
    except ValueError as ve:
        response_dict = {
            'error_code' : '-1',
            "info": str(ve)
        }
    return Response(response_dict)



def input(request):
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data["area"]
            bedrooms = form.cleaned_data["bedrooms"]
            bathrooms = form.cleaned_data["bathrooms"]
            stories = form.cleaned_data["stories"]
            mainroad = form.cleaned_data["mainroad"]
            guestroom = form.cleaned_data["guestroom"]
            basement = form.cleaned_data["basement"]
            hotwaterheating = form.cleaned_data["hotwaterheating"]
            airconditioning = form.cleaned_data["airconditioning"]
            parking = form.cleaned_data["parking"]
            prefarea = form.cleaned_data["prefarea"]
            furnished = form.cleaned_data["furnished"]
            # unfurnished = form.cleaned_data['unfurnished']
            if mainroad == "yes":
                mainroad = 0
            elif mainroad == "no":
                mainroad = 1
            else:
                return Response("Mainroad Field is invalid", status=400)

            if guestroom == "yes":
                guestroom = 0
            elif guestroom == "no":
                guestroom = 1
            else:
                return Response("Guestroom Field is invalid", status=400)

            if basement == "yes":
                basement = 0
            elif basement == "no":
                basement = 1
            else:
                return Response("Basement Field is invalid", status=400)

            if hotwaterheating == "yes":
                hotwaterheating = 0
            elif hotwaterheating == "no":
                hotwaterheating = 1
            else:
                return Response("HotWaterHeating Field is invalid", status=400)

            if airconditioning == "yes":
                airconditioning = 0
            elif airconditioning == "no":
                airconditioning = 1
            else:
                return Response("Air conditioning Field is invalid", status=400)

            if prefarea == "yes":
                prefarea = 0
            elif prefarea == "no":
                prefarea = 1
            else:
                return Response("Prefarea Field is invalid", status=400)
            if furnished == "semi_furnished":
                semi_furnished = 1
                unfurnished = 0
            elif furnished == "unfurnished":
                semi_furnished = 0
                unfurnished = 1
            else:
                return Response("Furnished Field is invalid", status=400)

            data = [
                area,
                bedrooms,
                bathrooms,
                stories,
                mainroad,
                guestroom,
                basement,
                hotwaterheating,
                airconditioning,
                parking,
                prefarea,
                semi_furnished,
                unfurnished,
            ]
            lin_reg_model = ApiConfig.model
            price_predicted = lin_reg_model.predict([data])
            price_predicted = int(price_predicted[0])
            messages.success(request, "Predicted Price is:{}".format(price_predicted))
            # print("price predicted",price_predicted)

    form = PredictForm()
    return render(request, "form.html", {"form": form})


