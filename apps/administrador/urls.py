from django.contrib import admin
from django.urls import path
from apps.administrador import views
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),    
    path('pos/', views.pos, name='pos'),
    path('medicamentos/', views.medicamentos, name='medicamentos'),
    url(r'^medicamentos/(\d+)/edit_medicamento', views.edit_medicamento,name='edit_medicamento'),    
    url(r'^medicamentos/delete_medicamento', views.delete_medicamento,name='delete_medicamento'),    
    path('añadir_medicamentos/', views.añadir_medicamentos, name='añadir_medicamentos'),    
    path('añadir_clientes/', views.añadir_clientes, name='añadir_clientes'),        
    path('clientes/', views.clientes, name='clientes'),
    url(r'^clientes/(\d+)/edit_cliente', views.edit_cliente,name='edit_cliente'),    
    url(r'^clientes/delete_cliente', views.delete_cliente,name='delete_cliente'),    
    path('registro_super/', views.registro_superusuario, name='registro_superusuario'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
