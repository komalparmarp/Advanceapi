from django.urls import path
from myapp import views

urlpatterns = [
    path('coupon_list/',views.coupon_list),
    path('coupon_detail/<int:pk>', views.coupon_detail),

]

