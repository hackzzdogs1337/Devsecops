from django.urls import path
from django.urls.conf import include
from shop.views import home,product_page
app_name='shop'
urlpatterns=[
    path('home/',name='home',view=home),
    path('single/',name='single',view=product_page)

]

