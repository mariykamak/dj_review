from django.urls import path
from rev_system import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail')

]
