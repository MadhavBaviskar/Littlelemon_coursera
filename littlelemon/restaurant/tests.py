from datetime import date,timedelta
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Category,MenuItem,Booking
class RestaurantAPITests(TestCase):
 def setUp(self):
  self.c=APIClient(); self.cat=Category.objects.create(title="Main",slug="main"); MenuItem.objects.create(title="Greek Salad",price="12.50",category=self.cat); self.tomorrow=date.today()+timedelta(days=1)
 def test_home_html(self): self.assertEqual(self.c.get("/").status_code,200)
 def test_menu_list(self): self.assertEqual(self.c.get("/api/menu-items/").status_code,200)
 def test_menu_write_protected(self): self.assertEqual(self.c.post("/api/menu-items/",{},format="json").status_code,401)
 def test_booking_create_authenticated(self):
  u=User.objects.create_user(username="guest",password="StrongPass123!"); self.c.force_authenticate(u); r=self.c.post("/api/bookings/",{"first_name":"Ava","reservation_date":self.tomorrow.isoformat(),"reservation_slot":18},format="json"); self.assertEqual(r.status_code,201)
 def test_duplicate_booking(self):
  Booking.objects.create(first_name="Ava",reservation_date=self.tomorrow,reservation_slot=18); u=User.objects.create_user(username="guest",password="StrongPass123!"); self.c.force_authenticate(u); r=self.c.post("/api/bookings/",{"first_name":"Sam","reservation_date":self.tomorrow.isoformat(),"reservation_slot":18},format="json"); self.assertEqual(r.status_code,400)
 def test_booking_date_filter(self):
  Booking.objects.create(first_name="Ava",reservation_date=self.tomorrow,reservation_slot=18); r=self.c.get("/api/bookings/",{"date":self.tomorrow.isoformat()}); self.assertEqual(r.status_code,200); self.assertEqual(r.data["count"],1)
