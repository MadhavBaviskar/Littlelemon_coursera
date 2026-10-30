from django.utils import timezone
from rest_framework import serializers
from .models import Category,MenuItem,Booking
class CategorySerializer(serializers.ModelSerializer):
 class Meta: model=Category; fields=["id","title","slug"]
class MenuItemSerializer(serializers.ModelSerializer):
 category=CategorySerializer(read_only=True)
 category_id=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),source="category",write_only=True)
 class Meta: model=MenuItem; fields=["id","title","price","featured","category","category_id"]
class BookingSerializer(serializers.ModelSerializer):
 class Meta: model=Booking; fields=["id","first_name","reservation_date","reservation_slot","created_at"]; read_only_fields=["id","created_at"]
 def validate_reservation_date(self,v):
  if v<timezone.localdate(): raise serializers.ValidationError("Reservation date cannot be in the past.")
  return v
 def validate(self,a):
  d=a.get("reservation_date",getattr(self.instance,"reservation_date",None)); s=a.get("reservation_slot",getattr(self.instance,"reservation_slot",None)); q=Booking.objects.filter(reservation_date=d,reservation_slot=s)
  if self.instance: q=q.exclude(pk=self.instance.pk)
  if d and s and q.exists(): raise serializers.ValidationError("This date and time are already booked.")
  return a
