import os
import json
from urllib.parse import urljoin

import requests

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from rooms.models import Room

payment_srv = os.environ.get('PAYMENT_SERVICE_ENDPOINT', 'http://srv-payment:8003')


@csrf_exempt
def book(request, room_id):
  room, _ = Room.objects.update_or_create(room_id=room_id, defaults={'is_booked': True})
  result = requests.post(urljoin(payment_srv, '/payments/', {'room_id': room_id}))
  return HttpResponse(json.dumps({
    "booked": True,
    "payment": result.json()
  }))


@csrf_exempt
def book404(request, room_id):
  raise Http404('did not find it. it is just not here')


@csrf_exempt
def error(request, room_id):
  raise TypeError('a custom error')

