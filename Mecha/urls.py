"""
URL configuration for Mecha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete, name='delete'),
    path('tasks_completed/', views.taskcomplete, name='taskcomplete'),
    path('tienda/', views.tienda, name='Tienda'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiaritems/<int:producto_id>/', views.limpiar_carrito_item, name="CLSK"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    path('gallery/', views.galeriaprueba, name='gallery'),
    path('productdetails/<int:producto_id>/', views.detalleproducto, name='PD'),
    path('cart/', views.cart, name='cart'),
    ]
if settings.DEBUG:
    # Configura la URL para servir archivos estáticos durante el desarrollo.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
