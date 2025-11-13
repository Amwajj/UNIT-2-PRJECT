from django.urls import path
from . import views


app_name = "main"

urlpatterns=[
    path('',views.home_view,name="home_view"),
    path('kings/',views.kings_view,name="kings_view"),
    path('security/',views.security_view,name="security_view"),
    path('health/',views.health_view,name="health_view"),
    path('organization/',views.organization_view,name="organization_view"),
    path('technology/',views.technology_view,name="technology_view"),
    path('health/',views.health_view,name="health_view"),
    path('services/',views.services_view,name="services_view"),
    path('mode/<mode>/',views.mode_view,name="mode_view"),
    path('dropdown/<state>/',views.dropdown_view,name="dropdown_view"),
    
]