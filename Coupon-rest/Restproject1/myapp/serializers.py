from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Coupon
from django.contrib.auth.models import User


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"






