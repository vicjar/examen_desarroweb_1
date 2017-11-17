"""autoSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from carros.views import CarList, CarDetail, CarCreate, CarDelete, CarUpdate

from carros.views import home
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^car$', CarList.as_view(), name='car_list'),
    url(r'^cardetail/(?P<id>[0-9]+)/$', CarDetail.as_view(), name='car_detail'),
    url(r'^create$', CarCreate.as_view(), name='CarCreate'),
    url(r'^cardelete/(?P<pk>[0-9]+)/$', CarDelete.as_view(), name='car_delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', CarUpdate.as_view(), name='car_update'),    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
