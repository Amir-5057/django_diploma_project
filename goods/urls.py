from django.urls import path

from goods import views

app_name = 'goods'



urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('catalog/<int:category_id>/', views.catalog, name='index'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('save_comment/<int:product_id>/', views.save_comment, name='save_comment'),
]





