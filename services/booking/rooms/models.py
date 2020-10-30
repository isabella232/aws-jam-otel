from django.db import models


class Room(models.Model):
  room_id = models.IntegerField()
  is_booked = models.BooleanField(default=False)