from datetime import date
from django.db import transaction,IntegrityError
from django.shortcuts import render
from rest_framework import viewsets,filters
from rest_framework.exceptions import ValidationError
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer
from .permissions import IsManagerOrReadOnly
class MenuItemViewSet(viewsets.ModelViewSet):
 queryset=MenuItem.objects.select_related("category").all(); serializer_class=MenuItemSerializer; permission_classes=[IsManagerOrReadOnly]
 filter_backends=[filters.SearchFilter,filters.OrderingFilter]; search_fields=["title","category__title"]; ordering_fields=["price","title"]
 def get_queryset(self):
  q=super().get_queryset(); c=self.request.query_params.get("category"); return q.filter(category_id=c) if c else q
class BookingViewSet(viewsets.ModelViewSet):
 queryset=Booking.objects.all(); serializer_class=BookingSerializer
 def get_queryset(self):
  q=super().get_queryset(); d=self.request.query_params.get("date")
  if d:
   try: d=date.fromisoformat(d)
   except ValueError: raise ValidationError({"date":"Use YYYY-MM-DD format."})
   q=q.filter(reservation_date=d)
  return q
 def perform_create(self,serializer):
  try:
   with transaction.atomic(): serializer.save()
  except IntegrityError: raise ValidationError({"detail":"This reservation slot is already booked."})
 def perform_update(self,serializer):
  try:
   with transaction.atomic(): serializer.save()
  except IntegrityError: raise ValidationError({"detail":"This reservation slot is already booked."})
