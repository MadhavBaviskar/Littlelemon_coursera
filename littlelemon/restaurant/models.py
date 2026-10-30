from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Category(models.Model):
 title=models.CharField(max_length=100,unique=True)
 slug=models.SlugField(max_length=110,unique=True)
 def __str__(self): return self.title
class MenuItem(models.Model):
 title=models.CharField(max_length=150)
 price=models.DecimalField(max_digits=7,decimal_places=2,validators=[MinValueValidator(0)])
 featured=models.BooleanField(default=False)
 category=models.ForeignKey(Category,related_name="menu_items",on_delete=models.PROTECT)
 def __str__(self): return self.title
class Booking(models.Model):
 first_name=models.CharField(max_length=100)
 reservation_date=models.DateField()
 reservation_slot=models.PositiveSmallIntegerField(choices=[(s,f"{s:02d}:00") for s in range(10,23)],validators=[MinValueValidator(10),MaxValueValidator(22)])
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=["reservation_date","reservation_slot"]
  constraints=[models.UniqueConstraint(fields=["reservation_date","reservation_slot"],name="unique_booking_date_slot")]
 def __str__(self): return f"{self.first_name} {self.reservation_date} {self.reservation_slot}:00"
