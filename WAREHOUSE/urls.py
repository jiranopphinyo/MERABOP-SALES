from django.urls import path
from WAREHOUSE.views_lot_number import *

app_name = "WAREHOUSE"
urlpatterns = [
    # PRODUCT LOT NUMBER
    path('product-lot-number/list/', product_lot_number_list, name="product_lot_number_list"),
    path('product-lot-number/detail/<str:id>/', product_lot_number_detail, name="product_lot_number_detail"),
    path('product-lot-number/create/', product_lot_number_create, name="product_lot_number_create"),
]
