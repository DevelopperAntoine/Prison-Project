"""prisonmis URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('script/',script),
    path('crimes/',crimes_view,name='crimes'),
    path('crimes/add',crime_add_view,name='crime_add'),
    path('crimes/<int:pk>/',crime_details_view,name='crime_details'),
    path('crimes/<int:pk>/update/',crime_update_view,name='crime_update'),
    path('crimes/<int:pk>/delete/',crime_delete_view,name='crime_delete'),
    path('leaves/',leaves_view,name='leaves'),
    path('leaves/add/',leave_add_view,name='leave_add'),
    path('leaves/<int:pk>/',leave_details_view,name='leave_details'),
    path('leaves/<int:pk>/update/',leave_update_view,name='leave_update'),
    path('leaves/<int:pk>/delete/',leave_delete_view,name='leave_delete'),
    path('',prisoners_view,name='prisoners'),
    path('add/',prisoner_add_view,name='prisoner_add'),
    path('<int:pk>/',prisoner_details_view,name='prisoner_details'),
    path('<int:pk>/update/',prisoner_update_view,name='prisoner_update'),
    path('<int:pk>/delete/',prisoner_delete_view,name='prisoner_delete'),
    path('visitors/',visitors_view,name='visitors'),
    path('visitors/add/',visitor_add_view,name='visitor_add'),
    path('visitors/<int:pk>/',visitor_details_view,name='visitor_details'),
    path('visitors/<int:pk>/update/',visitor_update_view,name='visitor_update'),
    path('visitors/<int:pk>/delete/',visitor_delete_view,name='visitor_delete'),
    path('transfers/',transfers_view,name='transfers'),
    path('transfers/add/',transfer_add_view,name='transfer_add'),
    path('transfers/<int:pk>/',transfer_details_view,name='transfer_details'),
    path('transfers/<int:pk>/update/',transfer_update_view,name='transfer_update'),
    path('transfers/<int:pk>/delete/',transfer_delete_view,name='transfer_delete'),
    path('releases/',releases_view,name='releases'),
    path('releases/<int:pk>/',release_form_view,name='release_form'),
    path('cells/',cells_view,name='cells'),
    path('cells/add/',cell_add_view,name='cell_add'),
    path('cells/<int:pk>/',cell_details_view,name='cell_details'),
    path('cells/<int:pk>/update/',cell_update_view,name='cell_update'),
    path('cells/<int:pk>/delete/',cell_delete_view,name='cell_delete'),
]
