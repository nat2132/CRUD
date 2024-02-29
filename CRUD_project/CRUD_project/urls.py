from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/', include('users_register.urls')),
    path('add/', views.products, name='add'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product')
]

