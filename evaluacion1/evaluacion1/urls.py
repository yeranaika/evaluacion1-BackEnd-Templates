"""
URL configuration for evaluacion1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# evaluacion1/urls.py

from django.contrib import admin
from django.urls import path
from home import views  # La importación es correcta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la página principal
    path('secundaria/', views.pagina_secundaria, name='pagina_secundaria'),  # Ruta para la página secundaria
    path('contacto/', views.contacto, name='contacto'),  # Ruta para la página de contacto
    path('test/', views.test_template, name='test_template'),

]
