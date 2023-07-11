from django.urls import path
from django.urls import path,include
from .views import PricePrediction
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api', views.PricePrediction)


urlpatterns = [
    path('index/',views.index),
    path('',views.input,name='myform'),
    path('api/',include(router.urls)),
    # path('status/', views.pricepredict),
    path('price/', views.pricepredict, name = 'price_prediction'),
   
]